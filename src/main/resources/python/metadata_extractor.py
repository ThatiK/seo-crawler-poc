from bs4 import BeautifulSoup
import requests

def fetch_metadata(url, user_agent, timeout):
    """
    Fetch and parse the HTML metadata of a given URL.

    Attempts to download the web page at the specified URL using the provided
    User-Agent and timeout settings. If successful, parses key SEO-relevant metadata
    such as the title, meta description, canonical link, H1 tag, and body content.

    Parameters:
    - url (str): The target URL to crawl.
    - user_agent (str): The User-Agent string to use in the request header.
    - timeout (int): Timeout value in seconds for the HTTP request.

    Returns:
    - dict: A dictionary with the following keys:
        - url (str)
        - title (str | None)
        - meta_description (str | None)
        - canonical (str | None)
        - h1 (str | None)
        - body (str | None)
        - error (str): Empty if successful, otherwise contains the error message.
    """
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

