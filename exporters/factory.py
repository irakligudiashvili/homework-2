from exporters import DataExporter, JSONExporter, XMLExporter
from constants import ExportFormat


class ExporterFactory:
    @staticmethod
    def get_exporter(export_format: ExportFormat) -> DataExporter:
        if export_format == ExportFormat.JSON:
            return JSONExporter()
        elif export_format == ExportFormat.XML:
            return XMLExporter()
        else:
            raise ValueError(f"Incorrect format: {export_format}")
