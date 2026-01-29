import pytest
from core.api_client import JSONPlaceholderClient

@pytest.fixture(scope="session")
def api():
    return JSONPlaceholderClient()

@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_multiple_posts(api, post_id):
    response = api.get_post(post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id
    assert "title" in response.json()

def test_create_post_modular(api, sample_payload):
    response = api.create_post(sample_payload)
    assert response.status_code == 201
    assert response.json()["title"] == sample_payload["title"]

@pytest.mark.parametrize("post_id", [1])
def test_update_post(api, post_id, update_payload):
    response = api.update_post(post_id, update_payload)
    assert response.status_code == 200
    assert response.json()["title"] == update_payload["title"]

@pytest.mark.parametrize("post_id", [1])
def test_delete_post(api, post_id):
    response = api.delete_post(post_id)
    assert response.status_code == 200