#  Small-api

_Python 3.11.2_   
_Fastapi 0.94.0_

Service exposes two endpoints:
-
1. blocks/{block_number: integer} [GET]
2. signatures/{signature: string} [GET]

In order to run the service:
-
1. Download the project
2. Navigate to the project directory
3. Install on your machine docker & docker-compose
4. Run: _make run-docker_

You can run service directly:
-
1. Create virtual environment
2. Install poetry or use pip instead
3. Run: poetry install or pip install requirements.txt
4. Run: make run

Tests:
-
In order to run test, run the following command: **_make test_**

Docs:
-
Once you have service running as follow: 

_INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)_

you can access Swagger by accessing **http://0.0.0.0:8080/docs**

