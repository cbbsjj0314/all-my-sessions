import logging
import requests
import json
import pendulum

from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import timedelta


def get_Redshift_connection(autocommit=True):
    hook = PostgresHook(postgres_conn_id='redshift_dev_db')
    conn = hook.get_conn()
    conn.autocommit = autocommit
    return conn.cursor()


@task
def extract(url):
    logging.info("extract started")

    response = requests.get(url)
    try:
        data = response.json()  # JSON 파싱
    except ValueError as e:
        logging.error("Error parsing JSON for URL: %s", url)
        raise

    if not data:
        logging.warning("No data returned for URL: %s", url)
    else:
        logging.info("Fetched data for URL: %s", url)
    
    logging.info("Extract ended")
    return data


@task
def transform(data):
    logging.info("Transform started")

    records = []

    for d in data:
        country = d["name"]["official"]
        population = d["population"]
        area = d["area"]
        records.append([country, population, area])

    logging.info("Transform ended")
    return records


@task
def load(schema, table, records):
    logging.info("Load started")

    cur = get_Redshift_connection()
    try:
        cur.execute("BEGIN;")

        ########## to_regclass()를 지원하지 않는 듯
        ########## PostgreSQL에선 가능한데 Redshift는 지원 안 한대
        # cur.execute(f"SELECT to_regclass('{schema}.{table}'::text);")  # 테이블 존재 여부 확인 => 존재하면 OID 반환, 없으면 NULL 반환
        # result = cur.fetchone()  # 반환된 값의 row 1개만 가져오는데 앞서 실행한 명령 덕에 OID or NULL이 저장됨
        # if result[0]:
        #     cur.execute(f"TRUNCATE TABLE {schema}.{table};")
        # else:
        #     logging.warning(f"Table {schema}.{table} does not exist. Skipping TRUNCATE.")
        
        # 테이블 존재 여부 확인
        cur.execute(f"""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = '{schema}'
            AND table_name = '{table}';
        """)
        result = cur.fetchone()

        if result[0] > 0:  # 겹치는 테이블 이름이 있을 수도 있으므로 > 0 조건을 사용함
            cur.execute(f"TRUNCATE TABLE {schema}.{table};")  # 테이블이 존재하면 TRUNCATE 실행
        else:
            logging.warning(f"Table {schema}.{table} does not exist. Skipping TRUNCATE.")

        try:
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {schema}.{table} (
                country VARCHAR(255),
                population BIGINT,
                area FLOAT
            );""")
        except Exception as e:
            logging.error(f"Error creating table {schema}.{table}: {e}")
            raise

        for r in records:
            country = r[0]
            population = r[1]
            area = r[2]

            sql = f"INSERT INTO {schema}.{table} (country, population, area) VALUES (%s, %s, %s);"
            cur.execute(sql, (country, population, area))

        cur.execute("COMMIT;")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        cur.execute("ROLLBACK;")
        raise

    logging.info("Load ended")


default_args = {
    'owner': 'BeomJun',
    'email': ['cbbsjj0314@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
}

with DAG(
    dag_id = 'update-country-info',
    start_date=pendulum.datetime(2024, 11, 1, tz="UTC"),  # UTC 시간대 설정
    catchup=False,
    tags=['api'],
    schedule = '30 6 * * 6',
    default_args=default_args
) as dag:
    
    records = transform(extract("https://restcountries.com/v3/all"))
    load("cbbsjj0314", "country_info", records)