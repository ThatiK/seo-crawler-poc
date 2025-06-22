# src/main/resources/python/crawler_core.py

import logging
from metadata_extractor import fetch_metadata
from robots_checker import is_allowed_by_robots
from classifier import classify_page
from topic_extractor import extract_topics

logger = logging.getLogger(__name__)

def process_url(url, config, use_ml=False):
    """
    Process a single URL and return metadata, classification, topics, or error.
    """
    user_agent = config.get("user_agent", "SEOPOCCrawlerBot/0.1")
    timeout = int(config.get("timeout", 5))

    result = {"url": url, "error": ""}

    try:
        if not is_allowed_by_robots(url, user_agent):
            logger.warning(f"Disallowed by robots.txt: {url}")
            result["error"] = "Disallowed by robots.txt"
        else:
            data = fetch_metadata(url, user_agent, timeout)
            if "error" in data:
                result["error"] = data["error"]
            else:
                result.update(data)
                result["classification"] = classify_page(data["body"], use_ml=use_ml)
                result["topics"] = extract_topics(data["body"])
    except Exception as e:
        logger.exception(f"Failed to process {url}")
        result["error"] = str(e)

    return result
