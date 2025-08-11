from loaders import DataLoader
from exporters import DataExporter
from handlers import RoomHandler


class App:
    def __init__(self, loader: DataLoader, exporter: DataExporter):
        self.loader = loader
        self.exporter = exporter

    def run(
            self,
            rooms_file: str,
            students_file: str,
            output_file: str
    ) -> None:
        rooms_data = self.loader.load(rooms_file)
        students_data = self.loader.load(students_file)

        handler = RoomHandler(rooms_data, students_data)
        rooms = handler.handle_data()

        self.exporter.export(rooms, output_file)
