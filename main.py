import json
from dataclasses import dataclass, field
from typing import List, Dict
from abc import ABC, abstractmethod
import xml.etree.ElementTree as etree
from xml.dom import minidom
import argparse
import sys


@dataclass
class Student:
    id: int
    name: str
    room: int


@dataclass
class Room:
    id: int
    name: str
    students: List[Student] = field(default_factory=list)

    def add_student(self, student: Student):
        self.students.append(student)


class DataLoader(ABC):
    @abstractmethod
    def load(self, file):
        pass


class JSONLoader(DataLoader):
    def load(self, file):
        try:
            with open(file) as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found: {file}")
            sys.exit(1)


class DataExporter(ABC):
    @abstractmethod
    def export(self, rooms: List[Room], file_name):
        pass


class JSONExporter(DataExporter):
    def export(self, rooms: List[Room], file_name):
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


class XMLExporter(DataExporter):
    def export(self, rooms: List[Room], file_name):
        file = file_name + ".xml"
        root = etree.Element("rooms")

        for room in rooms:
            room_elem = etree.SubElement(
                root,
                "room",
                id=str(room.id),
                name=room.name
            )

            students_elem = etree.SubElement(room_elem, "students")

            for student in room.students:
                etree.SubElement(
                    students_elem,
                    "student",
                    id=str(student.id),
                    name=student.name
                )

        rough_string = etree.tostring(root)
        pretty_xml = (
            minidom.parseString(rough_string)
            .toprettyxml(indent="    ")
        )

        with open(file, "w") as f:
            f.write(pretty_xml)


class RoomHandler:
    """
        Pairs the appropriate rooms and students
    """

    def __init__(self, rooms_data: List[Dict], students_data: List[Dict]):
        self.rooms_data = rooms_data
        self.students_data = students_data

    def handle_data(self):
        rooms = {
            room["id"]: Room(room["id"], room["name"])
            for room in self.rooms_data
        }

        for student in self.students_data:
            s = Student(student["id"], student["name"], student["room"])
            if s.room in rooms:
                rooms[s.room].add_student(s)

        return list(rooms.values())


class App:
    def __init__(self, loader: DataLoader, exporter: DataExporter):
        self.loader = loader
        self.exporter = exporter

    def run(self, rooms_file, students_file, output_file):
        rooms_data = self.loader.load(rooms_file)
        students_data = self.loader.load(students_file)

        handler = RoomHandler(rooms_data, students_data)
        rooms = handler.handle_data()

        self.exporter.export(rooms, output_file)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--rooms",
        required=True,
        help="File name for: rooms"
    )

    parser.add_argument(
        "--students",
        required=True,
        help="File name for: students"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="File name for: output"
    )

    parser.add_argument(
        "--format",
        required=True,
        choices=["json", "xml"],
        help="Output formats: JSON or XML"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    loader = JSONLoader()

    exporters = {
        "json": JSONExporter,
        "xml": XMLExporter
    }

    exporter = exporters[args.format]()

    app = App(loader, exporter)
    app.run(args.rooms, args.students, args.output)
    print(f"Data proccesed successfully into file: {args.output}.{args.format}")


if __name__ == "__main__":
    main()
