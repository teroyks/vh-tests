"""Run an execution until no output for a time given as a parameter."""

import json
import time
from pathlib import Path

import valohai
from valohai.paths import get_config_path

parameters = {
    "duration": 5,  # time without output before stopping the execution, in seconds
}

valohai.prepare(
    step="run-with-no-output-timeout",
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

    duration_with_output = duration + 5

    print(f"Running with output for {duration_with_output} seconds...")
    print("This part of the test should not be stopped.")

    for i in range(duration_with_output):
        time.sleep(1)
        print(f"{i + 1}", flush=True)
    print(f"✅ Ran for {duration_with_output} seconds.")

    duration_without_output = duration * 3
    print(
        f"Running without output for {duration_without_output} seconds unless stopped..."
    )
    print("The execution should be stopped before this part of the test is finished.")

    time.sleep(duration_without_output)
    print(
        f"❌ Ran for {duration_without_output} seconds without output and was not stopped."
    )


if __name__ == "__main__":
    main()
