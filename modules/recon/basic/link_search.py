import re
import requests
from ...handler.retry.retryrequest import RetryRequest
from ...config import Config
from messages import SuccessMessages, ErrorMessages

retry_request = RetryRequest(max_retries=3)
CONFIG = Config()


def detect_links_in_content(url: str):
    links_request = retry_request.retry(requests.get, f"{url}/", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
    if find_links(links_request):
        print(f"{SuccessMessages.FOUND_LINKS_IN_CONTENT} {find_links(links_request)[:CONFIG.display_link_amount()]} displaying {CONFIG.display_link_amount()} links")
    else:
        print(ErrorMessages.NO_LINKS_IN_CONTENT)


def find_links(content: str) -> list:
        """
        Finds links in a given string
        """
        links = []
        url_regex = re.compile(r'(?P<url>https?://[^\s]+)')
        for url in url_regex.findall(content):
            links.append(url)
        return links
