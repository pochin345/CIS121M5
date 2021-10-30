import unittest

from task import is_secret_word


# tests correct and incorrect word
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(is_secret_word("secret"), True, msg="if user enters 'secret', must be True")

    def test_add1(self):
        self.assertEqual(is_secret_word("s"), False, msg="if user does not enters 'secret', must be False")
