"""
This script contains tests for validating the streaming data endpoints
The endpoints require bearer token authentication.
"""

import pytest
import requests
import json

token = ""

@pytest.mark.parametrize(
    "endpoint",
    [
        "http://localhost:8000/sine",
        "http://localhost:8000/cosine",
        "http://localhost:8000/square",
        "http://localhost:8000/sawtooth",
        "http://localhost:8000/normal",
        "http://localhost:8000/uniform",
        "http://localhost:8000/exponential",
        "http://localhost:8000/anomalies/random",
        "http://localhost:8000/anomalies/random-square",
        "http://localhost:8000/anomalies/clustered",
        "http://localhost:8000/anomalies/periodic-spike",
        "http://localhost:8000/anomalies/count-per-duration"
    ],
)
def test_streaming_endpoint(endpoint):
    """
    Test the streaming endpoint by making requests to different endpoints and handling the streaming data.
    """
    headers = {"Authorization": f"Bearer {token}"}
    print(f"Testing endpoint: {endpoint}")
    try:
        response = requests.get(endpoint, headers=headers, stream=True)
        print(f"Response Status Code: {response.status_code}")
        assert (
            response.status_code == 200
        ), f"Failed to connect, status code: {response.status_code}"

        data = []
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                data.append(json.loads(decoded_line))
                print(f"Received data: {decoded_line}")
                if len(data) >= 10:
                    break
        assert len(data) > 0, "No data received from the stream"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")

if __name__ == "__main__":
    pytest.main()
