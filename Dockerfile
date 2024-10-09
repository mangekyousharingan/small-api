FROM python:3.13.0

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt && rm requirements.txt

COPY /src /code/src

WORKDIR /code/src

COPY docker-entrypoint.sh /usr/local/bin/entrypoint/docker-entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint/docker-entrypoint.sh"]
