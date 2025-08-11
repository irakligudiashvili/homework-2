from .data_exporter import DataExporter
from typing import List
from models import Room
import xml.etree.ElementTree as etree
from xml.dom import minidom


class XMLExporter(DataExporter):
    def export(self, rooms: List[Room], file_name: str) -> None:
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
