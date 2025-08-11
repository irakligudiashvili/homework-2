import argparse
from argparse import Namespace
from constants import ExportFormat


def parse_args() -> Namespace:
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
        choices=[fmt.value for fmt in ExportFormat],
        help=f"Output formats: {', '.join(fmt.value for fmt in ExportFormat)}"
    )

    return parser.parse_args()
