# syntax = docker/dockerfile:experimental
FROM python:3.8.5-buster

WORKDIR /data
COPY /data .

WORKDIR /app
ADD /app/requirement.txt .

RUN pip install -r requirement.txt

COPY /app .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80", "--reload"]