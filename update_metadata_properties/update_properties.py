"""Update input properties.

Loops through input files, checks if a specific property is set,
and if not, sets it to a random value between 1 and 100.
"""

import json
import logging
import os
import random
from collections import ChainMap
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx  # type: ignore

log = logging.getLogger(__name__)

# add additional DEBUG logging by setting the environment variable `DEBUG=1`
logging.basicConfig(level=logging.DEBUG if os.getenv("DEBUG") else logging.INFO)


CONFIG_DIR = Path("/valohai/config")
if not CONFIG_DIR.exists():
    # this part is only for testing the script locally --
    # not needed for running in Valohai
    log.debug("Running locally, using local directory as config dir.")
    CONFIG_DIR = Path(__file__).parent / "test_config"
    log.debug(CONFIG_DIR)

API_TOKEN = os.getenv("VALOHAI_API_TOKEN", "")
AUTH_HEADER = {"Authorization": f"Token {API_TOKEN}"}

# this is the property we want to add to the input files for this demo
TEST_PROPERTY = "my_prop"


def fetch_api_url() -> str:
    """Fetch the API URL from the API configuration.

    There probably is a better way to do this, but this works for now.
    """
    api_url_json = (CONFIG_DIR / "api.json").read_text()
    input_request_url = json.loads(api_url_json)["input_request"]["url"]
    help_url = urlparse(input_request_url)
    return f"{help_url.scheme}://{help_url.netloc}/api/v0"


API_URL = fetch_api_url()
log.debug(f"API URL: {API_URL}")


def fetch_input_metadata() -> dict:
    """Fetch input metadata from the configuration directory."""
    input_metadata_json = (CONFIG_DIR / "inputs.json").read_text()
    return json.loads(input_metadata_json)["input_files"]["files"]


def parse_properties(data: dict) -> dict:
    """Parse properties from input file metadata.

    Property metadata is stored in a list of dictionaries --
    only the first item is currently in use but this may change in the future.
    """

    # property metadata is optional in file metadata
    properties = data.get("metadata", [{}])

    # flatten the list of dictionaries into a single dictionary
    # [{"key": "value"}, {"key2": "value2"}, {}] -> {"key": "value", "key2": "value2"}
    return dict(ChainMap(*properties))


def parse_file_metadata(file_data: dict) -> tuple[str, dict]:
    """Parse file metadata to extract datum ID and properties."""
    datum_id = file_data["datum_id"]
    properties = parse_properties(file_data)
    log.debug(f"Parsed file metadata for {datum_id}: {properties}")
    return datum_id, properties


def set_property(datum_id: str, value: Any) -> None:
    """Set a property for a given datum ID.

    Note: this function updates the property for each file individually.
    In a real-world scenario, you should use the endpoint to update multiple files at once.
    """
    url = f"{API_URL}/data/{datum_id}/metadata/"
    data = {TEST_PROPERTY: value}
    try:
        response = httpx.post(url, headers=AUTH_HEADER, json=data)
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        log.error(f"Failed to update properties for {datum_id}: {e}")


for file_data in fetch_input_metadata():
    datum_id, properties = parse_file_metadata(file_data)

    log.debug(f"Processing datum {datum_id} with properties: {properties}")
    if TEST_PROPERTY not in properties:
        value = random.randint(1, 100)
        log.info(
            f"==> Updating {datum_id} properties to include {TEST_PROPERTY} = {value}."
        )
        set_property(datum_id, value)
    else:
        log.debug(f"Properties for {datum_id} already include 'my_prop': {properties}")
