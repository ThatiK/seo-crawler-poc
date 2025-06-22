# src/main/resources/python/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from crawler_core import process_url
from config_loader import load_config
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

class CrawlRequest(BaseModel):
    url: str
    env: str = "dev"
    use_ml: bool = False

@app.post("/crawl")
async def crawl(request: CrawlRequest):
    """
    Crawl a given web page and extract SEO metadata.

    This endpoint accepts a URL and returns key HTML metadata such as title,
    meta description, H1, canonical tag, main body text, and optionally performs
    classification ussing simple ML technique and topic extraction.

    It respects robots.txt rules and returns consistent JSON whether allowed or blocked.

    Request Body:
    - url (str): The full URL to crawl.
    - env (str, optional): Environment name to load config (default: "dev").
    - use_ml (bool, optional): If true, apply ML classification.

    Returns:
    - JSON object with:
        - url (str)
        - title (str | null)
        - meta_description (str | null)
        - h1 (str | null)
        - canonical (str | null)
        - body (str | null)
        - classification (str | null)
        - topics (List[str])
        - error (str): Empty if successful, otherwise failure reason.
    """
    logger.info(f"Received request: {request.url} [env={request.env}, ml={request.use_ml}]")
    config = load_config(request.env, "etc")
    result = process_url(request.url, config, request.use_ml)

    if result.get("error"):
        logger.warning(f"Failed to process {request.url}: {result['error']}")
    else:
        logger.info(f"Successfully processed {request.url}")

    return result

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring and platform readiness.
    """
    return {"status": "ok"}