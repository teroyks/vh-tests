# vh-tests

Miscellaneous Valohai testing

## Output Metadata

Miscellaneous testing of execution output properties (including adding files to a dataset).

### Steps

- `exec-config`: Log execution configuration details.
- `log-inputs`: Output input file contents to the execution log (to test input access).
- `properties-fixed-dataset-version`: Add a fixed dataset version to the output properties.
- `run-for-given-time`: Run an execution for n seconds (given as parameter) to test timeouts.
- `list-datum-data`: Show the path and size of a datum given as input.
- `get-dynamic-input-metadata`: Get input metadata from execution context without downloading the input files.

## Update Dependencies

```shell
make dev
```
