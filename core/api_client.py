import requests

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.session = requests.Session()
        self.session.headers.update({"Content-type": "application/json; charset=UTF-8"})

    def get_post(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, payload):
        return self.session.post(f"{self.base_url}/posts", json=payload)

    def update_post(self, post_id, payload):
        return self.session.put(f"{self.base_url}/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        return self.session.delete(f"{self.base_url}/posts/{post_id}")