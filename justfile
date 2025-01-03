dev:
    uv pip install -r requirements.txt --refresh --upgrade

run-adhoc-fixed-dataset-version:
    vh execution run --adhoc --title "fixed dataset exec" properties-fixed-dataset-version --nr-of-files=3

run-adhoc-print-execution-info:
    vh execution run --adhoc --title "execution info" exec-info

run-adhoc-execution-config:
    # vendor in valohai-utils until execution config support is released.
    make valohai-utils.tgz
    vh execution run --adhoc --title "execution.get_config" exec-config