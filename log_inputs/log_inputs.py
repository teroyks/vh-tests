"""Output content of input files to the execution log.

Input can be a datum or a dataset URL.

Run locally:
python log_inputs/log_inputs.py --input_data <LOCAL_FILE_PATH>

Run execution:
vh execution run log-inputs --input-data <INPUT_URL>

INPUT_URL can be either a datum url (datum://...) or a dataset version (dataset://...).
"""

from pathlib import Path
import valohai

valohai.prepare(
    step="log-inputs",
    default_inputs={"input_data": []},
)

for file_path in valohai.inputs("input_data").paths():
    print(f"Input datum: {file_path}:")
    print("=" * 20)
    content = Path(file_path).read_text()
    print(content)
    print("-" * 80)
