"""
Test what happens when you run an execution that tries to
create a dataset version with the same name as an existing dataset version.

Test: run the execution twice in a row.

Expected behaviour: the second execution creates the outputs but does not create a new dataset version,
there is an alert attached to the execution noting that the dataset version already exists.
"""

import logging
from pathlib import Path

import valohai

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Define the step for valohai.yaml

default_parameters = {
    "nr_of_files": 10,
}

valohai.prepare(
    step="properties-fixed-dataset-version",
    image="ghcr.io/astral-sh/uv:python3.12-bookworm-slim",
    default_parameters=default_parameters,
)

output_dir = "same-dataset-version"

# fixed, so the dataset creation is successful only on the first execution
dataset_name = "properties-fixed-dataset-version"
dataset_version = "v1"

nr_of_files = valohai.parameters("nr_of_files").value
output_path = valohai.outputs(output_dir)

with valohai.output_properties() as properties:
    dataset_version_uri = properties.dataset_version_uri(dataset_name, dataset_version)
    for file_nr in range(nr_of_files):
        file_path = Path(output_path.path(f"file-{file_nr}.txt"))
        file_path.write_text(f"This is file {file_nr}")

        relative_file_path = Path(output_dir) / file_path.name

        # Add metadata for the file
        properties.add(
            file=relative_file_path,
            properties={
                "index": file_nr,
            },
        )

        # Add file to a dataset
        properties.add_to_dataset(
            file=relative_file_path, dataset_version=dataset_version_uri
        )
