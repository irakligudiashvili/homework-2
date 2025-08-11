from .data_loader import DataLoader
import json
import sys
from typing import Any


class JSONLoader(DataLoader):
    def load(self, file: str) -> Any:
        try:
            with open(file) as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found: {file}")
            sys.exit(1)
