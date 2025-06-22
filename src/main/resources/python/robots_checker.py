from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

parser_cache = {}

def is_allowed_by_robots(url, user_agent):
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
