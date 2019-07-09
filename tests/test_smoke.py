from http import HTTPStatus

from tests import BaseTestCase


class TestSmoke(BaseTestCase):

    def test_smoke(self):
        response = self.client.get("/mono-statistics/smoke")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json["status"], "success")
        self.assertEqual(response.json["message"], "ok")
        self.assertIn("response_datetime", response.json.keys())
