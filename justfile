run-adhoc-fixed-dataset-version:
    vh execution run --adhoc --title "fixed dataset exec" properties-fixed-dataset-version --nr-of-files=3

run-adhoc-print-execution-info:
    vh execution run --adhoc --title "execution info" exec-info

run-adhoc-execution-config:
    # vendor in valohai-utils until execution config support is released.
    make valohai-utils.tgz
    vh execution run --adhoc --title "execution.get_config" exec-config

run-execution-with-time-limit:
    # run a longer execution with a time limit defined in the config YAML
    # the execution will be terminated after 20 seconds
    vh execution run --adhoc --title "execution with time limit" run-for-limited-time