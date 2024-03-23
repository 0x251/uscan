import requests

from messages import SuccessMessages, ErrorMessages
from ...handler.logger.log import log_data_to_file
from ...handler.retry.retryrequest import RetryRequest
from ...config import Config

CONFIG = Config()

def detect_debug_log(url: str) -> None:
    retry_request = RetryRequest(max_retries=3)
    debug_request = retry_request.retry(requests.get, f"{url}/debug.log", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).status_code
    if debug_request != 200:
        print(ErrorMessages.NO_DEBUG_LOG)
    if debug_request == 200:
        print(f"{SuccessMessages.FOUND_DEBUG_LOG} {url}/debug.log")