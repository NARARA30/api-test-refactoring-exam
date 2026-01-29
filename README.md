### 📋 작업 프로세스

### Phase 1-1. 로컬 프로토타입 구현 (No Design Pattern)

- **방식:** `pytest` + `requests` 모듈 조합
- **내용:** 디자인 패턴 없이 직관적인 스크립트 작성
- **범위:** GET, POST, PUT, PATCH, DELETE 등 주요 메소드 자유 선택
- **포인트:** 기능 동작 검증(Status Code, Response Body) 위주로 빠르게 구현

### Phase 1-2. (선택) Postman & Newman

- **작업 순서:**
    1. Postman에서 API Request 생성 및 테스트 스크립트 작성
    2. Collection 저장 및 JSON 파일 Export
    3. CLI 환경에서 **Newman**을 이용하여 해당 Collection 일괄 실행 및 결과 확인

### Phase 2. 프레임워크 리팩토링 (Optimization)

- **기반 레포:** [pytest-framework-exam-v2](https://www.google.com/search?q=https://github.com/DevYeop/pytest-framework-exam-v2)
- **작업 내용:** Phase 1-1에서 작성한 코드를 위 repo의 프레임워크 구조에 맞춰 리팩토링

- **핵심:** 유지보수와 확장성을 고려한 구조적 개선
