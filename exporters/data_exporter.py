from abc import ABC, abstractmethod
from typing import List
from models import Room


class DataExporter(ABC):
    @abstractmethod
    def export(self, rooms: List[Room], file_name: str) -> None:
        pass
