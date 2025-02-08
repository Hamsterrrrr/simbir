FROM python:3.12

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH=/app

CMD ["pytest"]

