import requests
from messages import ErrorMessages
class RetryRequest:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries

    def retry(self, func, *args, **kwargs):
        retries = 0
        while retries < self.max_retries:
            try:
                response = func(*args, **kwargs)
                return response
            except Exception as e:
                #print(e)
                retries += 1
        print(ErrorMessages.RETRY_ERROR)
        return requests.Response()