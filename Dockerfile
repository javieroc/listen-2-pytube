FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app

COPY ./app/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./app ./
