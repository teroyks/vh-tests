"""Print out some execution-related information."""

import json
import logging
from pathlib import Path

import valohai
from valohai.config import is_running_in_valohai
from valohai.internals import global_state
from valohai.internals.guid import get_execution_guid
from valohai.paths import get_config_path

log = logging.getLogger(__name__)

valohai.prepare(
    step="exec-info",
    image="ghcr.io/astral-sh/uv:python3.12-bookworm-slim",
)

execution_guid = get_execution_guid()
print(f"Execution GUID: {execution_guid}")

running_in_valohai = is_running_in_valohai()
print(f"Running in Valohai: {running_in_valohai}")

print(f"Step name: {global_state.step_name}")

print(f"Inputs: {global_state.inputs}")
print(f"Parameters: {global_state.parameters}")

config_path = Path(get_config_path())
print(f"Config path: {config_path}")
output_dir = valohai.outputs()
print(f"Output path: {output_dir}")
try:
    for item in config_path.iterdir():
        print(item)
        # copy files as outputs for inspection
        if item.is_file():
            output_file = Path(output_dir.path(item.name))
            output_file.write_bytes(item.read_bytes())

    execution_config_file = config_path / "execution.json"
    execution_config = json.loads(execution_config_file.read_bytes())
    print(execution_config)
except FileNotFoundError:
    log.warning("⚠️ Config path or execution config does not exist")
except ValueError:
    log.warning("⚠️ Error reading config file: not JSON")
