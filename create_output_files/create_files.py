"""Create output files (of fixed size).

The number and size of the outputs are given as parameters.
"""

import os
import random
import string
from pathlib import Path

import humanfriendly
import valohai
from faker import Faker

default_parameters = {"nr_of_files": 1, "file_size": "1KiB"}

valohai.prepare(
    step="create-output-files",
    image="",
    default_parameters=default_parameters,
)

output_dir = "output-files"

nr_of_files = valohai.parameters("nr_of_files").value
file_size_bytes = humanfriendly.parse_size(valohai.parameters("file_size").value)
output_path = valohai.outputs(output_dir)
random_file_prefix = "".join(random.choice(string.ascii_lowercase) for _ in range(4))

fake = Faker()

for _ in range(nr_of_files):
    file_name = f"{random_file_prefix}_{fake.file_name(extension='dat')}"
    file_content = os.urandom(file_size_bytes)

    output_file = Path(output_path.path(file_name))
    print(f"Creating {output_file} ...")
    output_file.write_bytes(file_content)
