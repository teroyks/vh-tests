"""Call Valohai API from an execution."""

import httpx

from helpers.valohai import get_api_url

API_URL = get_api_url()

print(f"API URL: {API_URL}")

# Calling the plain API URL should return a list of available endpoints.
httpx_response = httpx.get(API_URL, timeout=10)
if httpx_response.status_code == 200:
    print("API call successful")
else:
    print(f"Failed to reach API. Status code: {httpx_response.status_code}")
    print("Response content:", httpx_response.text)
