import unittest
from mirrorClock import mirrorClock


class WhatIsTheTime(unittest.TestCase):

    # positive tests

    def test_empty_string_input(self):
        # Если на вход не дано ничего или дана пустая строка (не имеет значение длина такой строки)
        clock = mirrorClock()
        self.assertEqual("", clock.what_is_the_time())

    def test_input_12_00_time(self):
        clock = mirrorClock()
        inputData = "12:00"
        rightOutputData = "12:00"
        self.assertEqual(rightOutputData, clock.what_is_the_time(inputData))

    def test_input_11_hours_time(self):
        # проверка, чтобы 11:00 было 01:00 и при отражении времени больше 11 часов, но меньше 12 не получаем значение hh как 00 (допустимый формат hh от 01 до 12)
        clock = mirrorClock()
        inputData = "11:05"
        rightOutputData = "12:55"
        self.assertEqual(rightOutputData, clock.what_is_the_time(inputData))

    def test_different_time(self):
        clock = mirrorClock()
        inputData = "05:25"
        rightOutputData = "06:35"
        self.assertEqual(rightOutputData, clock.what_is_the_time(inputData))

    # negative tests
    def test_string_with_spaces_only(self):
        # Если на вход пришли одни пробелы, то выдать ошибку
        clock = mirrorClock()
        inputData = "  "
        with self.assertRaises(ValueError):
            clock.what_is_the_time(inputData)

    def test_not_string_type_for_input_raises_exception(self):
        # Если на вход дано НЕ str, а int, список, массив или что-то другое
        clock = mirrorClock()
        inputData = 10
        with self.assertRaises(ValueError):
            clock.what_is_the_time(inputData)

    def test_for_wrong_time_input(self):
        # Если на вход пришла строка с некорректным временем (формат времени hh:mm)
        clock = mirrorClock()
        inputData = "18:00"
        with self.assertRaises(ValueError):
            clock.what_is_the_time(inputData)

    def test_for_illegal_symbols_input(self):
        # Если на вход пришла строка с некорректными символами
        clock = mirrorClock()
        inputData = "+ 13:00 /"
        with self.assertRaises(ValueError):
            clock.what_is_the_time(inputData)


if __name__ == "__main__":
    unittest.main()
