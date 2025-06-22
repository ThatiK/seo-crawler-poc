FROM python:3.11-slim

WORKDIR /app

COPY src/main/resources/python /app
COPY requirements.txt .
COPY src/main/resources/etc /app/etc
RUN mkdir /app/nltk_data

ENV NLTK_DATA=/app/nltk_data

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
