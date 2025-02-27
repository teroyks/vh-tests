"""Run an execution for a time given as a parameter."""

import time

import valohai

parameters = {
    "duration": 20,  # time to run the script for, in seconds
}

valohai.prepare(
    step="run-for-given-time",
    default_parameters=parameters,
)


def main():
    duration = int(valohai.parameters("duration").value)

    print(f"Running for {duration} seconds...")
    for i in range(duration):
        time.sleep(1)
        print(f"{i + 1}", flush=True)
    print(f"Ran for {duration} seconds.")


if __name__ == "__main__":
    main()
