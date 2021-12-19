FROM python:3.9.7-alpine
ARG APP_USER=myapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]