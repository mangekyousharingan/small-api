FROM python:3.11.2

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt && rm requirements.txt

COPY /src /code/src

WORKDIR /code/src

CMD ["python", "main.py"]
