import json

from messages import DetectionMessages

class Config(DetectionMessages):
    def __init__(self) -> None:
        with open('config.json', 'r') as config:
            self.json_dump = json.loads(config.read())

    def threads(self) -> int:
        if self.json_dump['threads'] > 30:
            print(self.THREADS_WARN)
        return self.json_dump['threads']

    def useragent(self) -> str:
        if "Uscan" not in self.json_dump['useragent']:
            print(self.USERAGENT_WARN)
        return self.json_dump['useragent']

    def timeouts(self) -> int:
        return self.json_dump['timeouts']

    def enable_exploits(self) -> bool:
        return self.json_dump['enable-exploits']

    def enable_recon(self) -> bool:
        return self.json_dump['enable-recon']

    def logging(self) -> bool:
        return self.json_dump['logging']

    def display_link_amount(self) -> int:
        return self.json_dump['link-display-amount']