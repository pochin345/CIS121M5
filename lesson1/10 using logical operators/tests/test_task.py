import unittest

from ..task import is_minimum_age, is_match_name, is_winner


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_age_21(self):
        self.assertEqual(is_minimum_age(21), True, msg="is_minimum_age age 21 should be True")

    def test_age_20(self):
        self.assertEqual(is_minimum_age(20), False, msg="is_minimum_age age 20 should be False")

    def test_name_John(self):
        self.assertEqual(is_match_name("John"), True, msg="is_match_name name John should be True")

    def test_name_Mary(self):
        self.assertEqual(is_match_name("Mary"), True, msg="is_match_name name Mary should be True")

    def test_name_Johnny(self):
        self.assertEqual(is_match_name("Johnny"), False, msg="is_match_name name Johnny should be False")

    def test_name_MaryEllen(self):
        self.assertEqual(is_match_name("Mary Ellen"), False, msg="is_match_name name Mary Ellen should be False")

    def test_winner_John_21(self):
        self.assertEqual(is_winner("John", 21), True, msg="is_winner: John, 21 should be a winner")

    def test_winner_Mary_21(self):
        self.assertEqual(is_winner("Mary", 21), True, msg="is_winner: Mary, 21 should be a winner")

    def test_winner_John_20(self):
        self.assertEqual(is_winner("John", 20), False, msg="is_winner: John, 20 should not be a winner")

    def test_winner_Mary_20(self):
        self.assertEqual(is_winner("Mary", 20), False, msg="is_winner: Mary, 20 should not be a winner")

    def test_winner_Johnny_21(self):
        self.assertEqual(is_winner("Johnny", 21), False, msg="is_winner: John, 20 should not be a winner")

    def test_winner_MaryEllen_20(self):
        self.assertEqual(is_winner("Mary Ellen", 20), False, msg="is_winner: Mary, 20 should not be a winner")
