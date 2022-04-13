import unittest
import sqlite3 as sl
from DatabaseTime import DatabaseTime

class CountTime(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseTime()

    def test_input_right_time(self):
        self.assertEqual(self.database.convertTimeAndAddToDB("04:55"), "07:05")

    def test_input_empty_string(self):
        # Если на вход пришла строка вида ""
        self.assertEqual(self.database.convertTimeAndAddToDB(""), "")

    def test_input_right_time_with_bad_symbols(self):
        with self.assertRaises(ValueError):
            self.database.convertTimeAndAddToDB("04:55 : v")

    def test_input_not_string(self):
        with self.assertRaises(ValueError):
            self.database.convertTimeAndAddToDB([1, 2, 3])

    def test_input_incorrect_1_to_12_hours(self):
        with self.assertRaises(ValueError):
            self.database.convertTimeAndAddToDB("18:00")


if __name__ == "__main__":
    unittest.main()

