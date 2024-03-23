

from .logging import Logging
from ...config import Config
from json import dumps
from random import getrandbits
from datetime import datetime
from messages import SuccessMessages

import logging, re

JSON_DATA = [
    {
        "detect":
            {
                "cms": "",
                "version": "",
                "themes": "",
                "users": "",
                "plugin": ""
            },
        "info":
            {
                "seed":"",
                "url": "",
                "ip": "",
                "serverType": "",
                "contentType": "",
                "X_pingback": "",
                "Server": "",
                "Strict-Transport-Security": "",
                "Content-Security-Policy": "",
                "X-Content-Type-Options": "",
                "Cross-Origin-Resource-Policy": "",
                "Cloudflare": "",
                "dns-a": "",
                "dns-mx": "",
                "dns-txt": "",
                "dns-ns": ""
            },
        "links":
            {
                "sqlvuln": "",
                "subdomains": "",
                "urls": ""
            }
    },
    ]

class ResultLogger(Logging):
    def log_json(self, obj: str, url_saved: list, data: str, type: str):
        create_seed = self.create_uuid()
        get_current_time = self.get_current_time()
        if type:
            url_saved[0]['info']['url'] = data
            url_saved[0]['info']['seed'] = create_seed
            url = self.strip_http_from_url(data)
            self.save_uscan_log(url, get_current_time, url_saved)
            print(SuccessMessages.LOGGED_TO_FILE + f"results/{str(url)}-{get_current_time[1]}.json - {get_current_time[0]}")

    def create_uuid(self) -> int:
        # generate random bit UUID for result log
        return getrandbits(53) * 3

    def get_current_time(self) -> tuple[str, str]:
        # get the time and date of result log
        now = datetime.now()
        return now.strftime("%H:%M:%S"), now.strftime("%H-%M-%S")

    def strip_http_from_url(self, data: str) -> str:
        url = re.compile(r"https?://(www\.)?")
        return url.sub('', data).strip().strip('/')

    def save_uscan_log(self, url: str, get_current_time: tuple[str, str], url_saved: list) -> None:
        with open(f'results/{str(url)}-{get_current_time[1]}.json', 'a+') as log:
            log.write(dumps(url_saved, indent=3)+'\n')

def log_data_to_file(data: str, obj:str, type: str):
    CONFIG = Config()
    if not CONFIG.logging():
        return
    if obj == "detect":
        JSON_DATA[0]["detect"][type] = data
    elif obj == "info":
        JSON_DATA[0]["info"][type] = data
    elif obj == "links":
        JSON_DATA[0]["links"][type] = data
    elif type:
        LOGGER = ResultLogger()
        LOGGER.log_json(obj, JSON_DATA, data, type)