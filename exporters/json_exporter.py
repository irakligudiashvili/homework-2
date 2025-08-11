from .data_exporter import DataExporter
from typing import List
from models import Room
import json


class JSONExporter(DataExporter):
    def export(self, rooms: List[Room], file_name: str) -> None:
        file = file_name + ".json"
        data = []

        for room in rooms:
            data.append({
                "id": room.id,
                "name": room.name,
                "students": [{
                    "id": student.id,
                    "name": student.name
                }
                    for student in room.students
                ]
            })

        with open(file, "w") as f:
            json.dump(data, f, indent=4)
