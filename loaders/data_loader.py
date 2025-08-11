from abc import ABC, abstractmethod
from typing import Any


class DataLoader(ABC):
    @abstractmethod
    def load(self, file: str) -> Any:
        pass
