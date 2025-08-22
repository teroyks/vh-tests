# Update File Properties

Demonstrate processing the properties for input files
and update them in an execution without touching the actual files.

The properties can be read from the inputs metadata file,
and the update is done via the API.

## Usage

### Authentication

To access the API, you need to create an authentication token in Valohai
and set it to the `VALOHAI_API_TOKEN` environment variable.

### Running the Execution

Create an execution in Valohai, choose the `update-input-properties` step.
Add the files you want to update as inputs
(either by choosing existing files, or giving a dataset version URL as input).

Run the execution.

### How does it work?

The script reads the input metadata file,
which contains the properties of the input files.
It does not actually download the input files.

The demo script checks for the existence of a property `my_prop`.
If it does not exist, it adds the properto to the file
with a random number as the value.

_Note:_ When configuring the step inputs,
make sure to include the `download: on-demand` directive
to avoid downloading the files unnecessarily.

_Note:_ This script updates each file with a separate API call.
This is just to demonstate the functionality;
for a large number of files, you should use the batch API to update multiple files at once.