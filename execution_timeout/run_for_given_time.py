"""Run an execution for a time given as a parameter."""

import json
import time
from pathlib import Path

import valohai
from valohai.paths import get_config_path

parameters = {
    "duration": 20,  # time to run the script for, in seconds
}

valohai.prepare(
    step="run-for-given-time",
    default_parameters=parameters,
)


def get_execution_config() -> dict:
    config_file = Path(get_config_path()) / "execution.json"
    try:
        return json.loads(config_file.read_text())
    except FileNotFoundError:
        return {}


def get_runtime_config() -> dict:
    config_file = Path(get_config_path()) / "runtime.json"
    try:
        return json.loads(config_file.read_text())
    except FileNotFoundError:
        return {}


def main():
    duration = int(valohai.parameters("duration").value)

    print("Execution config:")
    print(json.dumps(get_execution_config(), indent=2))

    print("Runtime config:")
    print(json.dumps(get_runtime_config(), indent=2))

    print(f"Running for {duration} seconds...")

    for i in range(duration):
        time.sleep(1)
        print(f"{i + 1}", flush=True)
    print(f"Ran for {duration} seconds.")


if __name__ == "__main__":
    main()
