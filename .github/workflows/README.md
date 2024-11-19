# Workflows for the hangman_web Directory

The following workflows, **test-hangman-web.yml** and **docker-image.yml**, are designed specifically for the **hangman_web** directory. These YAML files reference this directory and perform their respective actions as described below.

## Directory Details

- Path: all-my-sessions/docker-practice/webservice-with-docker/hangman_web

- GitHub Repository Link: hangman_web Directory

### test-hangman-web.yml

This workflow is used to run tests and perform code linting for Python files in the hangman_web directory. Pay attention to the **paths:** and **run:** sections, which ensure that the workflow targets the correct files and executes the appropriate commands.

### docker-image.yml

This workflow is used to build and push a Docker image for the **hangman_web** application. The docker build command uses the **hangman_web** directory as its build context.
