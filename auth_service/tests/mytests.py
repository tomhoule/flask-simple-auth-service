from unittest import TestCase
from auth_service import routes
from auth_service.server import app

class HelloTestCase(TestCase):

    def test_it_works(self):
        self.assertTrue(True)


class APITests(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_returns_200(self):
        res = self.app.get('/api/v1/')
        assert "Coucou" in res.data.decode()
        assert res.status_code == 200
