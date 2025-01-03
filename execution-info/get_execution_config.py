"""Fetch execution info from config helper."""

import valohai.execution

execution_config = valohai.execution.get_config()

print(f"Execution ID: {execution_config.id}")
print(f"Execution title: {execution_config.title}")
print(f"Execution counter: {execution_config.counter}")
