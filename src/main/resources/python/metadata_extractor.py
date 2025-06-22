from bs4 import BeautifulSoup
import requests

def fetch_metadata(url, user_agent, timeout):
    try:
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        return {
            "url": url,
            "title": soup.title.string.strip() if soup.title else "",
            "meta_description": (soup.find("meta", attrs={"name": "description"}) or {}).get("content", ""),
            "body": soup.body.get_text(separator=" ", strip=True) if soup.body else "",
            "h1": soup.find("h1").text.strip() if soup.find("h1") else "",
            "canonical": (soup.find("link", rel="canonical") or {}).get("href", "")
        }

    except Exception as e:
        return {
            "url": url,
            "title": "",
            "meta_description": "",
            "h1": "",
            "canonical": "",
            "body": "",
            "error": str(e)
        }

