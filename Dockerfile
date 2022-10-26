FROM python:3.10
WORKDIR /app
RUN pip install pipenv
COPY Pipfile.lock Pipfile.lock
RUN pipenv sync
EXPOSE 8000
CMD pipenv run uvicorn main:app --host 0.0.0.0
COPY main /app