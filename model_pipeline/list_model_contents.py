"""List the contents of a model.

Input should be a model URL.
"""

import valohai

valohai.prepare(
    step="list-model-contents",
    default_inputs={"model": ""},
)

print("Model contents:")
for file_path in valohai.inputs("model").paths():
    print(f"- {file_path}")

print("\nDone")
