from fastapi.testclient import TestClient
# import json
from main import app

# Create a TestClient instance
client = TestClient(app)


def test_get_all_items():
    # Send a GET request to the '/items' endpoint
    response = client.get("/")

    # Assert that the response status code is 200 OK
    assert response.status_code == 200

    # Assert that the response body contains the expected items
    expected_items = [{"total": 8192.0, "used": 2926.297, "id": 1, "free": 149.781},
                      {"total": 8192.0, "used": 2798.297, "id": 2, "free": 139.828}]
    assert response.json() == expected_items
