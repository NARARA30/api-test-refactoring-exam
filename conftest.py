import pytest
from core.api_client import JSONPlaceholderClient

@pytest.fixture
def common_headers():
    return {"Content-type": "application/json; charset=UTF-8"}

@pytest.fixture
def sample_payload():
    return {
        "title": "모듈화 테스트",
        "body": "Fixture를 활용한 본문 내용",
        "userId": 1
    }

@pytest.fixture
def update_payload():
    return {
        "id": 1,
        "title": "수정된 제목",
        "body": "내용 업데이트 완료",
        "userId": 1
    }
    
@pytest.fixture(scope="session")
def api():
    return JSONPlaceholderClient()
