from unittest import TestCase
from auth_service.server import app


class APITests(TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_index_returns_200(self):
        res = self.app.get("/api/v1/")
        assert "Coucou" in res.data.decode()
        assert res.status_code == 200

    def test_admin_decorator_lets_admins_in(self):
        res = self.app.get(
            "/api/v1/admin", headers={"Authenticate": "i am the admin"})
        assert "passé" in res.data.decode()
        assert res.status_code == 200

    def test_admin_decorator_rejects_unauthenticated(self):
        res = self.app.get("/api/v1/admin")
        self.assertEqual(res.status_code, 401, res.data)

    def test_admin_decorator_rejects_non_admins(self):
        res = self.app.get(
                "/api/v1/admin", headers={"Authenticate": "i am a banana"})
        self.assertEqual(res.status_code, 403, res.data)
