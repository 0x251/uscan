from enum import Enum
from abc import ABC, abstractmethod

class Logging(ABC):
    @property
    @abstractmethod
    def log_json(self):
        ...
    @property
    @abstractmethod
    def create_uuid(self) -> int:
        ...
    @property
    @abstractmethod
    def get_current_time(self) -> str:
        ...
    @property
    @abstractmethod
    def strip_http_from_url(self) -> str:
        ...
    @property
    @abstractmethod
    def save_uscan_log(self) -> None:
        ...