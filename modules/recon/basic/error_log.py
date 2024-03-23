import requests
from ...handler.retry.retryrequest import RetryRequest
from messages import SuccessMessages
from ...config import Config

error_log_path = ["error_log", "error_log.txt", "errorlog.sql", "error_log.sql", "errorlog.json", "error_log.json", "error_map"]
retry_request = RetryRequest(max_retries=3)
CONFIG = Config()


def detect_error_log(url: str):
    for error_log_paths in error_log_path:
        error_log_request = retry_request.retry(requests.get, f"{url}/{error_log_paths}", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()})
        if error_log_request.status_code == 200:
            if "mysql" in error_log_request.text:
                print(f"{SuccessMessages.FOUND_ERROR_LOG}{url}/{error_log_paths}")
