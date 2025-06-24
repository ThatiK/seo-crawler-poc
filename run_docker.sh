#!/bin/bash

# Variables
TAG="seo-metadata-crawler"
INPUT_FILE=${1:-input.txt}
OUTPUT_FILE=${2:-output.csv}

# Build the image
docker build -t $TAG .

# Run the container with volume mounts
docker run --rm \
  -v $(pwd)/$INPUT_FILE:/app/input.txt \
  -v $(pwd)/$OUTPUT_FILE:/app/output.csv \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/gcp-key.json \
  -v $(pwd)/gcp-key.json:/app/gcp-key.json \
  $TAG \
  --input input.txt \
  --output output.csv \
  --env dev \
  --config-base-path /app/etc
