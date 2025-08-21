"""Miscellaneous helper functions for Valohai integration."""

import json
from pathlib import Path
from urllib.parse import urlparse


from valohai.paths import get_config_path  # type: ignore


def get_api_url() -> str:
    """Parse the Valohai API URL from configuration.

    Raises FileNotFoundError if the configuration file is not found.
    """
    config_file = Path(get_config_path()) / "api.json"
    api_config = json.loads(config_file.read_text())
    input_request_url = api_config["set_status_detail"]["url"]
    help_url = urlparse(input_request_url)
    return f"{help_url.scheme}://{help_url.netloc}/api/v0"
