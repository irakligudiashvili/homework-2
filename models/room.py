from dataclasses import dataclass, field
from typing import List
from .student import Student


@dataclass
class Room:
    id: int
    name: str
    students: List[Student] = field(default_factory=list)

    def add_student(self, student: Student) -> None:
        self.students.append(student)
