import httpx
from ..handler.retry.retryrequest import RetryRequest
from ..config import Config
from messages import SuccessMessages

CONFIG = Config()
retry_request = RetryRequest(max_retries=2)

PERMISSION_PATTERNS = [
    "drwxr-xr-x",  # Directory Permissions
    "-rw-r--r--",  # File read/write permissions for owner, read for others
    "-rw-rw-rw-",  # File read/write permissions for everyone
    "lrwxrwxrwx",  # Symbolic link permissions
    "drwxr-xr-x"   # Duplicate Directory Permissions
]

class NoCMS:
    @staticmethod
    def detect_listing(url: str) -> None:
        response = retry_request.retry(httpx.get, f"{url}/.listing", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()})
        if any(permission in response.text for permission in PERMISSION_PATTERNS):
            print(f"{SuccessMessages.FOUND_LISTING} {response.url}")

