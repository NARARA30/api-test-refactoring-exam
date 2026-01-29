import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_multiple_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id
    assert "title" in response.json()

def test_create_post_modular(common_headers, sample_payload):
    response = requests.post(
        f"{BASE_URL}/posts", 
        json=sample_payload, 
        headers=common_headers
    )
    assert response.status_code == 201
    assert response.json()["title"] == sample_payload["title"]

@pytest.mark.parametrize("post_id", [1])
def test_update_post(post_id, update_payload):
    response = requests.put(
        f"{BASE_URL}/posts/{post_id}", 
        json=update_payload
    )
    assert response.status_code == 200
    assert response.json()["title"] == update_payload["title"]

@pytest.mark.parametrize("post_id", [1])
def test_delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200