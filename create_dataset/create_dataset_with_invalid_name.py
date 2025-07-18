"""
Test what happens when you try to create a dataset with invalid name.

Dataset names should contain only lowercase letters, numbers, dots, underscores, and dashes.
"""

from pathlib import Path
import time

import valohai

output_dir = "invalid_dataset_name_test"

dataset_name = "Dataset"  # upper case letter is not allowed
dataset_version = time.time()

with valohai.output_properties() as properties:
    dataset_version_uri = properties.dataset_version_uri(dataset_name, dataset_version)
    output_path = valohai.outputs(output_dir)

    # Create a file to be added to the dataset
    file_path = Path(output_path.path("file.txt"))
    file_path.write_text("This is a test file for invalid dataset name.")

    relative_file_path = Path(output_dir) / file_path.name
    properties.add_to_dataset(
        file=relative_file_path, dataset_version=dataset_version_uri
    )
