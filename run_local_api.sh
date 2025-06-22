#!/bin/bash

TAG="seo-metadata-api"
PORT=8080

echo "========================================"
echo "Building Docker image: $TAG"
echo "Exposing API at: http://localhost:$PORT/crawl"
echo "========================================"

docker build -t $TAG .

echo "Running container..."
docker run --rm -p $PORT:8080 \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/gcp-key.json \
  -v $(pwd)/gcp-key.json:/app/gcp-key.json \
  $TAG
