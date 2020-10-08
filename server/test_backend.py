import pytest,json

from app import app

class TestClass:
    def test_hello_world(self):
        with app.test_client(self) as tester:
            response = tester.get('/ping', content_type='html/text')
            assert response.status_code == 200
            assert response.data == b'Flask says: Hello World!'

    def test_books(self):
        with app.test_client(self) as tester:
            response = tester.get('/books', content_type='html/text')
            assert response.status_code == 200
            data = response.get_data(as_text=True)
            data = json.loads(data)
            assert data['status'] == 'success'
