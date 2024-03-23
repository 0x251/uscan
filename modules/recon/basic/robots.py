import requests
from messages import SuccessMessages, ErrorMessages
from ...handler.retry.retryrequest import RetryRequest
from ...handler.logger.log import log_data_to_file
from ...config import Config

CONFIG = Config()

def enumrate_robots_txt(response: list[str]) -> None:
    disallowed_data = [f"{SuccessMessages.FOUND_DISALLOW_ROBOTS} {data}" for data in response if "Disallow" in data]
    if len(disallowed_data) > 2:
        print('\n'.join(disallowed_data))

def detect_robots_txt(url: str) -> None:
    retry_request = RetryRequest(max_retries=3)
    request = retry_request.retry(requests.get, f"{url}/robots.txt", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()})
    if request.status_code != 200:
        print(ErrorMessages.NO_ROBOTS_TXT)
    if request.status_code == 200:
        print(f"{SuccessMessages.FOUND_ROBOTS_TXT} {url}/robots.txt")
        enumrate_robots_txt(request.text.split('\n'))
