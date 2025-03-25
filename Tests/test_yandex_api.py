import requests
import pytest
from Tests.config import TOKEN


API_URL = "https://cloud-api.yandex.net/v1/disk/resources"
TOKEN = TOKEN
HEADERS = {"Authorization": f"OAuth {TOKEN}"}


@pytest.mark.parametrize("folder_name, expected_code", [
    ("test_folder", 201),
    ("existing_folder", 409),
])
def test_create_folder(folder_name, expected_code):
    if expected_code == 201:
        response = requests.put(f"{API_URL}?path={folder_name}", headers=HEADERS)
        assert response.status_code == expected_code
        check_response = requests.get(f"{API_URL}?path={folder_name}", headers=HEADERS)
        assert check_response.status_code == 200
        requests.delete(f"{API_URL}?path={folder_name}", headers=HEADERS)
    elif expected_code == 409:
        requests.put(f"{API_URL}?path={folder_name}", headers=HEADERS)
        response = requests.put(f"{API_URL}?path={folder_name}", headers=HEADERS)
        assert response.status_code == expected_code
        requests.delete(f"{API_URL}?path={folder_name}", headers=HEADERS)


def test_create_folder_unauthorized():
    response = requests.put(f"{API_URL}?path=unauthorized_folder", headers={"Authorization": "OAuth invalid"})
    assert response.status_code == 401
