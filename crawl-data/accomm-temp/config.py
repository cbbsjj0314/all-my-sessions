# crawl_main_page.ipynb와 crawl_detail_page.ipynb에서 쓰이는 dict, list가 들어있는 파일

###############################
### generate_url에 쓰이는 인수 ###
###############################
region_dict = {
    "경기": "%EA%B2%BD%EA%B8%B0",
    "제주도": "%EC%A0%9C%EC%A3%BC%EB%8F%84",
    "충남": "%EC%B6%A9%EB%82%A8",
    "인천": "%EC%9D%B8%EC%B2%9C",
    "대구": "%EB%8C%80%EA%B5%AC",
    "대전": "%EB%8C%80%EC%A0%84",
    "서울": "%EC%84%9C%EC%9A%B8",
    "경남": "%EA%B2%BD%EB%82%A8",
    "부산": "%EB%B6%80%EC%82%B0",
    "전북": "%EC%A0%84%EB%B6%81",
    "울산": "%EC%9A%B8%EC%82%B0",
    "광주": "%EA%B4%91%EC%A3%BC",
    "강원": "%EA%B0%95%EC%9B%90",
    "경북": "%EA%B2%BD%EB%B6%81",
    "전남": "%EC%A0%84%EB%82%A8",
    "충북": "%EC%B6%A9%EB%B6%81",
    "세종": "%EC%84%B8%EC%A2%85",
}

weekday_dates = ['2024-11-04', '2024-11-05']
holiday_dates = ['2024-11-09', '2024-11-10']

category_codes = {
    '전체': 0,
    '모텔': 1,
    '호텔': 2,  # 호텔, 리조트
    '펜션': 3,
    '홈&빌라': 15,
    '캠핑': 5,
    '게하': 6  # 게스트하우스, 한옥
}

###############################
#### 세부 페이지의 부대시설 dict ###
###############################
motel_facilities_dict = {
    '트윈베드': False,
    '파티룸': False,
    '스파/월풀': False,
    '수영장': False,
    '공주룸': False,
    '노천탕': False,
    '거울룸': False,
    '히노끼탕': False,
    '맛사지 베드': False,
    '반신욕': False,
    '욕실 TV': False,
    '호수뷰': False,
    '복층룸': False,
    '바다뷰': False,
    '하늘뷰': False,
    '야외테라스': False,
    '빔프로젝터': False,
    '사우나/찜질방': False,
    '3D TV': False,
    '당구대': False,
    '미니바': False,
    '게임기': False
}
