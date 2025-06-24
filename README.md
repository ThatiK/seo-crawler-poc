# SEO Metadata Crawler – Part 1 (BrightEdge PoC)

This project is a proof-of-concept metadata crawler that can:
- Crawl a single web page
- Extract SEO-relevant metadata (title, description, headings, etc.)
- Classify the page content
- Extract relevant topics
- Serve results via CLI or FastAPI API

## Architecture

- Language: Python 3.11
- Deployed via: Docker, GitHub Actions, Google Cloud Run
- Uses:
  - `requests`, `BeautifulSoup` for crawling
  - `nltk` for topic extraction
  - `scikit-learn` for optional ML-based classification (enabled via `--use-ml`; otherwise rule-based)
  - `fastapi` for API interface

---

## Usage (CLI)

```bash
python src/main/resources/python/main.py \
  --input input.txt \
  --output output.csv \
  --env dev \
  --config-base-path src/main/resources/etc \
  --use-ml
```

- `--input` and `--output`: Can be local or GCS paths (e.g., `gs://...`)
- `--env`: Loads config from `dev.ini` or `prod.ini`
- `--use-ml`: Enables ML-based classifier



## Bot User-Agent Setup

This crawler uses a custom bot User-Agent registered for this PoC.  
The implementation and metadata for the bot are maintained in the [project GitHub repository](https://github.com/ThatiK/seo-crawler-poc).

We respect `robots.txt` rules and identify our crawler via:

User-Agent: SEO-Metadata-Crawler/1.0 (+https://thatik.github.io/seo-crawler-poc)

---

## Usage (API)

Deployed to Cloud Run. Use the `/crawl` endpoint:

### POST `/crawl`

**Request:**
```json
{
  "url": "https://www.example.com",
  "env": "dev",
  "use_ml": false
}
```

**Response:**
```json
{
  "url": "...",
  "title": "...",
  "meta_description": "...",
  "h1": "...",
  "canonical": "...",
  "body": "...",
  "classification": "...",
  "topics": ["...", "..."],
  "error": ""
}
```

**Health check:**
```bash
GET /health
```

---

## Deployment

1. Dockerized and tested locally using:

```bash
./run_local_api.sh
```

2. CI/CD via GitHub Actions
3. Deploys automatically to Cloud Run using Workload Identity Federation (keyless)

---

## Project Structure

```
src/
└── main/
    └── resources/
        ├── python/
        │   ├── main.py          # CLI batch runner
        │   ├── app.py           # FastAPI service
        │   ├── crawler_core.py  # Shared crawling logic
        │   └── ...              # utils, config loader, topic extractor, etc.
        ├── etc/
        │   ├── dev.ini
        │   └── prod.ini
```

---

## Example Test URLs

Use these for local or API testing:

- http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster
- http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/
- http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/
