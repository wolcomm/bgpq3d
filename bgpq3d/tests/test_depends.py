from unittest import TestCase
from whichcraft import which


class TestNull(TestCase):
    def test_null(self):
        self.assertTrue(True)

class TestBgpq3(TestCase):
    def test_which(self):
        path = which('bgpq3')
        self.assertTrue(isinstance(path, str))
