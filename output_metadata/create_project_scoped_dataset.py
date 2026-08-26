"""
Output a file, creating a project-scoped dataset with metadata.
"""

import datetime
import json
import logging

import valohai

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

current_date = datetime.date.today().isoformat()
current_datetime = datetime.datetime.now().isoformat()
test_project_id = "01942b47-f0d8-0021-c074-87370badadee"

# Define the step for valohai.yaml
default_parameters = {
    "dataset_name": f"project-scoped-dataset-{current_date}",
    "project_id": test_project_id,
}

valohai.prepare(
    step="create-project-scoped-dataset",
    image="ghcr.io/astral-sh/uv:python3.14-trixie-slim",
    default_parameters=default_parameters,
)

output_dir = "project-scoped-dataset-output"

dataset_name = str(valohai.parameters("dataset_name").value)
dataset_version = "v1"
associated_project_id = valohai.parameters("project_id").value

if not dataset_name:
    raise ValueError("Dataset name parameter is required.")

metadata = {
    "valohai.dataset-versions": [
        {
            "uri": f"dataset://{dataset_name}/{dataset_version}",
            "associated_project_ids": [associated_project_id],
        }
    ]
}

output_path = valohai.outputs(output_dir)
file_path = output_path.path(f"example-file-{current_datetime}.txt")

log.info(f"Writing file {file_path}")

with open(file_path, "w") as f:
    f.write("This is an example file in a project-scoped dataset.\n")
    log.info("Output file created successfully.")

metadata_file_path = f"{file_path}.metadata.json"

log.info(f"Writing metadata file {metadata_file_path}")
log.info(f"Metadata to be added: {metadata}")

with open(metadata_file_path, "w") as f:
    json.dump(metadata, f, indent=2)
    log.info("Metadata file created successfully.")

exit()

# using output_properties does not seem to be working...
try:
    with valohai.output_properties() as properties:
        if not dataset_name:
            raise ValueError("Dataset name parameter is required.")
        dataset_version_uri = properties.dataset_version_uri(
            dataset_name, dataset_version
        )

        output_path = valohai.outputs(output_dir)
        file_path = output_path.path(f"example-file-{current_datetime}.txt")

        log.info(f"Dataset version URI: {dataset_version_uri}")
        log.info(f"Project ID: {associated_project_id}")
        log.info(f"Writing file {file_path}")

        with open(file_path, "w") as f:
            f.write("This is an example file in a project-scoped dataset.\n")

        relative_file_path = f"{output_dir}/example-file.txt"

        # Add metadata for the file
        properties.add(
            file=relative_file_path,
            properties={
                "test-prop": "foo",
                "valohai.dataset-versions": [
                    {
                        "uri": dataset_version_uri,
                        "associated_project_ids": [associated_project_id],
                    },
                ],
            },
        )
except TypeError:
    pass
