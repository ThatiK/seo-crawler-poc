#!/bin/bash

# Default values
ENV=${1:-dev}
INPUT_PATH=${2:-input.txt}
OUTPUT_PATH=${3:-output.csv}
CONFIG_BASE_PATH="etc"

echo "========================================"
echo "Running SEO Metadata Crawler"
echo "Environment      : $ENV"
echo "Input file       : $INPUT_PATH"
echo "Output file      : $OUTPUT_PATH"
echo "Config path base : $CONFIG_BASE_PATH"
echo "========================================"


# Run the crawler
python3 python/crawl_runner.py \
  --env "$ENV" \
  --input "$INPUT_PATH" \
  --output "$OUTPUT_PATH" \
  --config-base-path "$CONFIG_BASE_PATH"
