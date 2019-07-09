from unittest import TestCase

from core.app import app


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = app.test_client()
