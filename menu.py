
import threading
from abc       import ABC, abstractmethod


class MenuTriggers(ABC):
    @property
    @abstractmethod
    def run(self) -> bool: ...

class ScanUrl(MenuTriggers):
    def run(self, scan: object):
        t1 = threading.Thread(target=scan)
        t1.start()
        t1.join()