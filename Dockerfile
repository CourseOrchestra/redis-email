FROM python:3.7-alpine
RUN mkdir -p /src
WORKDIR /src
ENV PYTHONBUFFERED 1

COPY ./Pipfile ./Pipfile.lock ./
RUN pip install --no-cache-dir Pipenv
RUN pipenv lock -r > requirements.txt
# install requirements
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["rq", "worker"]
