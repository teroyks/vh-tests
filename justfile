run-adhoc-fixed-dataset-version:
    vh execution run --adhoc --title "fixed dataset exec" properties-fixed-dataset-version --nr-of-files=3

run-adhoc-print-execution-info:
    vh execution run --adhoc --title "execution info" exec-info

run-adhoc-execution-config:
    # vendor in valohai-utils until execution config support is released.
    make valohai-utils.tgz
    vh execution run --adhoc --title "execution.get_config" exec-config

run-execution-with-time-limit args='':
    # run a longer execution with a time limit defined in the config YAML
    # the execution will be terminated after 20 seconds
    vh execution run --title "execution with time limit" run-for-limited-time {{ args }}

run-execution-with-no-output-limit:
    # run a longer execution with no output limit defined in the config YAML
    # the execution will be terminated after --duration=N seconds
    vh execution run --title "execution with no-output limit" run-with-no-output-timeout --watch --adhoc

simple-pipeline-run-step:
    # run the pipeline step with default parameter
    @echo "Starting execution -- should output 'Hello, Valohai!'"
    vh execution run --adhoc --watch pipeline-hello

simple-pipeline-run:
    vh pipeline run --adhoc simple-pipeline --greet-name="Just Pipeline"

run-execution-list-model-contents:
    # run an execution that lists the contents of a model
    vh execution run --adhoc --watch --title "list model contents" list-model-contents --model-url=model://test-model/1

model-pipeline-run:
    # run a pipeline that uses a model -- use default parameters
    vh pipeline run --adhoc model-pipeline
