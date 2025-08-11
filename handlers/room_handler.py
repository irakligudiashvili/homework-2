from typing import List, Dict
from models import Room, Student


class RoomHandler:
    """
    Pairs the appropriate rooms and students
    """

    def __init__(self, rooms_data: List[Dict], students_data: List[Dict]):
        self.rooms_data = rooms_data
        self.students_data = students_data

    def handle_data(self) -> List[Room]:
        rooms = {
            room["id"]: Room(room["id"], room["name"])
            for room in self.rooms_data
        }

        for student in self.students_data:
            s = Student(student["id"], student["name"], student["room"])
            if s.room in rooms:
                rooms[s.room].add_student(s)

        return list(rooms.values())
