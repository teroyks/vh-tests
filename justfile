dev:
    uv pip install -r requirements.txt --refresh --upgrade

run-adhoc-fixed-dataset-version:
    vh execution run --adhoc --title "fixed dataset exec" properties-fixed-dataset-version --nr-of-files=3
