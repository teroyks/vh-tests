"""List information about a datum."""

from pathlib import Path

import valohai

valohai.prepare(
    step="list-datum-data",
    default_inputs={"datum": ""},
)

datum = valohai.inputs("datum").path()
if datum:
    print(f"Datum URL: {datum}")
    file_path = Path(datum)
    file_size = file_path.stat().st_size

    print(f"File path: {file_path}")
    print(f"File size: {file_size} bytes")
