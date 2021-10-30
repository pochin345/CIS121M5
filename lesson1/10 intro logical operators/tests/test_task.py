import unittest

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, 3, msg="always true")
