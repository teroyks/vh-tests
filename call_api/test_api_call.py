"""Call Valohai API from an execution."""

from helpers.valohai import get_api_url

API_URL = get_api_url()

print(f"API URL: {API_URL}")
