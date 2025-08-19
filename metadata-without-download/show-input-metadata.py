"""Display metadata from an input file without downloading it.

Note: valohai-utils cannot be used in this script because it automatically downloads the file.

When configuring this script in Valohai, add the following to the step configuration:
```yaml
inputs:
  download: on-demand
```

Read more:
- https://docs.valohai.com/hc/en-us/articles/31598381149457-On-Demand-Input-Downloads
- https://valohai.gitbook.io/valohai-docs/projects/data-versioning/dynamic-inputs
"""

from collections import ChainMap
import json

# fetch execution config

from pathlib import Path

CONFIG_DIR = Path("/valohai/config")
if not CONFIG_DIR.exists():
    print("Running locally, using current directory as config dir.")
    CONFIG_DIR = Path(".")


def parse_metadata(data: dict) -> dict:
    """Parse metadata from input data.

    Metadata is stored in a list of dictionaries --
    only the first item is currently in use but this may change in the future.
    """

    # property metadata is optional – default is a list with one empty dict
    properties = data.get("metadata", [{}])

    # flatten the list of dictionaries into a single dictionary
    # [{"key": "value"}, {"key2": "value2"}, {}] -> {"key": "value", "key2": "value2"}
    return dict(ChainMap(*properties))


# fetch input metadata
input_metadata_json = (CONFIG_DIR / "inputs.json").read_text()
input_metadata = json.loads(input_metadata_json)

# fetch input file properties
for file_data in input_metadata["input_files"]["files"]:
    print(f"{file_data['datum_id']}: {parse_metadata(file_data)}")
