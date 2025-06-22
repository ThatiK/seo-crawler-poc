from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

parser_cache = {}

def is_allowed_by_robots(url, user_agent):
    """
    Check if the given URL is allowed to be crawled based on robots.txt.

    Downloads and parses the site's robots.txt file, and checks whether
    the specified User-Agent is allowed to fetch the given URL.

    Parameters:
    - url (str): The target page URL.
    - user_agent (str): The User-Agent used by the crawler.

    Returns:
    - bool: True if the URL is allowed by robots.txt, False otherwise.
    """
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    if base_url not in parser_cache:
        robots_url = f"{base_url}/robots.txt"
        rp = RobotFileParser()
        try:
            rp.set_url(robots_url)
            rp.read()
            parser_cache[base_url] = rp
        except Exception as e:
            # If robots.txt can't be read, assume allowed
            return True

    rp = parser_cache[base_url]
    return rp.can_fetch(user_agent, url)
