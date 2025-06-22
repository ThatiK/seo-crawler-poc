FROM python:3.11-slim

WORKDIR /app

ENV NLTK_DATA=/app/nltk_data

COPY src/main/resources/python /app
COPY nltk_data /app/nltk_data
COPY requirements.txt .
COPY src/main/resources/etc /app/etc

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
