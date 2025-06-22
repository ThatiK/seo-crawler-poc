# src/main/resources/python/app.py

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from crawler_core import process_url
from config_loader import load_config

app = FastAPI()

class CrawlRequest(BaseModel):
    url: str
    env: str = "dev"
    use_ml: bool = False

@app.post("/crawl")
async def crawl(request: CrawlRequest):
    config = load_config(request.env, "etc")
    result = process_url(request.url, config, request.use_ml)

    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["error"])
    
    # return raw result including topics list
    return result
