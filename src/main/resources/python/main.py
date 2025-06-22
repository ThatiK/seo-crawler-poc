import os, sys
import argparse
import csv
import logging
from config_loader import load_config
from crawler_core import process_url
from gcs_utils import read_urls_from_gcs, write_csv_to_gcs
from metadata_extractor import fetch_metadata
from robots_checker import is_allowed_by_robots
from classifier import classify_page
from topic_extractor import extract_topics

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("[%(asctime)s] (%(levelname)s) %(message)s"))
logger.addHandler(handler)

def read_urls(path):
    if path.startswith("gs://"):
        return read_urls_from_gcs(path)
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def write_results(rows, path, fieldnames):
    if path.startswith("gs://"):
        write_csv_to_gcs(rows, path, fieldnames)
    else:
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow({k: row.get(k, "") for k in fieldnames})

def run(input_path, output_path, env, config_base_path, use_ml):
    config = load_config(env, config_base_path)
    urls = read_urls(input_path)
    logger.info(f"Loaded {len(urls)} URLs")

    results = []
    fieldnames = ["url", "title", "meta_description", "h1", "canonical", "body", "classification", "topics", "error"]

    for url in urls:
        result = process_url(url, config, use_ml)
        result["topics"] = ", ".join(result.get("topics", []))  
        results.append(result)

    write_results(results, output_path, fieldnames)
    logger.info(f"Results written to {output_path}")




if __name__ == "__main__":
    def usage():
        return """
        SEO Metadata Crawler - Part 1 (BrightEdge PoC)

        Usage:
          python3 crawl_runner.py --input <file_or_gs_path> --output <file_or_gs_path> [options]

        Required:
          --input               Path to input file (local or gs://)
          --output              Path to output CSV (local or gs://)

        Optional:
          --env                 Environment to load config for (default: dev)
          --config-base-path    Base path to config .ini files (default: src/main/resources/etc)
          --use-ml              Use ML classifier instead of rule-based
          --help                Show this help message

        Example:
          python3 crawl_runner.py --input input.txt --output results.csv --env dev
          python3 crawl_runner.py --input gs://bucket/urls.txt --output gs://bucket/out.csv --env prod --use-ml
        """

    parser = argparse.ArgumentParser(
        description="SEO Metadata Crawler",
        usage=usage()
    )
    
    parser.add_argument("--input", required=True, help="Input file path (local or gs://)")
    parser.add_argument("--output", required=True, help="Output CSV path (local or gs://)")
    parser.add_argument("--env", default="dev", help="Environment name (e.g., dev or prod)")
    parser.add_argument("--config-base-path", default="src/main/resources/etc", help="Base path to .ini files")
    parser.add_argument("--use-ml", action="store_true", help="Enable ML-based classification")

    args = parser.parse_args()

    run(
        input_path=args.input,
        output_path=args.output,
        env=args.env,
        config_base_path=args.config_base_path,
        use_ml=args.use_ml
    )
