import requests

def test_get_single_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "title" in response.json()

def test_create_post():
    payload = {
        "title": "실무자 테스트",
        "body": "하드코딩 버전 내용임",
        "userId": 1
    }
    headers = {"Content-type": "application/json; charset=UTF-8"}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", 
        json=payload, 
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()["title"] == "실무자 테스트"

def test_update_post():
    payload = {
        "id": 1,
        "title": "수정된 제목",
        "body": "내용 업데이트 완료",
        "userId": 1
    }
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1", 
        json=payload
    )
    assert response.status_code == 200
    assert response.json()["title"] == "수정된 제목"

def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200