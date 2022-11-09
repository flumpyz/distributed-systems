FROM python:3.10
WORKDIR /app
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install pipenv
COPY Pipfile.lock Pipfile.lock
RUN pipenv sync
EXPOSE 8000
CMD pipenv run uvicorn main:app --host 0.0.0.0
COPY . /app