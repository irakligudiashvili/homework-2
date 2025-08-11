from cli import parse_args
from loaders import JSONLoader
from exporters import ExporterFactory
from constants import ExportFormat
from app import App


def main():
    args = parse_args()

    loader = JSONLoader()

    exporter = ExporterFactory.get_exporter(ExportFormat(args.format))

    app = App(loader, exporter)
    app.run(args.rooms, args.students, args.output)
    print(f"Data proccesed successfully into file: {args.output}.{args.format}")


if __name__ == "__main__":
    main()
