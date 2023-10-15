#!/usr/bin/env python3
"""
Plik: operations_test.py
Autor: Stanisław Polak
Data utworzenia: 08-10-2023
Data modyfikacji: 08-10-2023
Wersja: 1.0
Opis: Testy do ćwiczenia 2.
"""
import importlib
import unittest
import operations  # Twój moduł

USING_PYTEST = True
# Jeżeli jest zainstalowany moduł "pytest"
#if importlib.util.find_spec("pytest") is not None: - nie dziala :(
if USING_PYTEST:
    # Użyj testów Pytest
    print("Proszę uruchomić testy za pomocą komendy 'pytest'")
    def test_first_character():
        assert operations.first_character("abcdefg") == "a"
        assert operations.first_character("12345") == "1"
        assert operations.first_character("A") == "A"
    def test_first_two_characters():
        assert operations.first_two_characters("abcdefg") == "ab"
        assert operations.first_two_characters("12345") == "12"
        assert operations.first_two_characters("A") == ""  # Ciąg "A" jest za krótki.
    def test_all_characters_except_first_two():
        assert operations.all_characters_except_first_two("abcdefg") == "cdefg"
        assert operations.all_characters_except_first_two("12345") == "345"
        assert (
            operations.all_characters_except_first_two("A") == ""
        )  # Ciąg "A" jest za krótki.
    def test_penultimate_character():
        assert operations.penultimate_character("abcdefg") == "f"
        assert operations.penultimate_character("12345") == "4"
        assert operations.penultimate_character("A") == ""  # Ciąg "A" jest za krótki.
    def test_last_three_characters():
        assert operations.last_three_characters("abcdefg") == "efg"
        assert operations.last_three_characters("12345") == "345"
        assert operations.last_three_characters("A") == ""  # Ciąg "A" jest za krótki.
    def test_all_characters_in_even_positions():
        assert operations.all_characters_in_even_positions("abcdefg") == "aceg"
        assert operations.all_characters_in_even_positions("12345") == "135"
        assert operations.all_characters_in_even_positions("A") == "A"
    def test_merge_characters_and_duplicate():
        assert operations.merge_characters_and_duplicate("Programowanie Skryptowe") == "PwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPw"
        assert operations.merge_characters_and_duplicate("") == ""
        assert operations.merge_characters_and_duplicate("X") == "X"
        assert operations.merge_characters_and_duplicate("ab")== "aaaa"
    
else:
    # Użyj testów Unittest
    # Jeżeli nazwa importowanego modułu jest znana w momencie tworzenia skryptu, to można go zaimportować, na przykład, tak:
    # import unittest
    # Jeśli nazwa importowanego modułu jest znana dopiero podczas działania / uruchamiania skryptu — np. jest przekazywana w linii komend (jest napisem), to trzeba go zaimportować w następujący sposób:
    # unittest = importlib.import_module("unittest")
    class Test_TestTextOperations(unittest.TestCase):
        def test_first_character(self):
            self.assertEqual(operations.first_character("abcdefg"), "a")
            self.assertEqual(operations.first_character("12345"), "1")
            self.assertEqual(operations.first_character("A"), "A")
        def test_first_two_characters(self):
            self.assertEqual(operations.first_two_characters("abcdefg"), "ab")
            self.assertEqual(operations.first_two_characters("12345"), "12")
            self.assertEqual(
                operations.first_two_characters("A"), ""
            )  # Ciąg "A" jest za krótki.
        def test_all_characters_except_first_two(self):
            self.assertEqual(
                operations.all_characters_except_first_two("abcdefg"), "cdefg"
            )
            self.assertEqual(operations.all_characters_except_first_two("12345"), "345")
            self.assertEqual(
                operations.all_characters_except_first_two("A"), ""
            )  # Ciąg "A" jest za krótki.
        def test_penultimate_character(self):
            self.assertEqual(operations.penultimate_character("abcdefg"), "f")
            self.assertEqual(operations.penultimate_character("12345"), "4")
            self.assertEqual(
                operations.penultimate_character("A"), ""
            )  # Ciąg "A" jest za krótki.
        def test_last_three_characters(self):
            self.assertEqual(operations.last_three_characters("abcdefg"), "efg")
            self.assertEqual(operations.last_three_characters("12345"), "345")
            self.assertEqual(
                operations.last_three_characters("A"), ""
            )  # Ciąg "A" jest za krótki.
        def test_all_characters_in_even_positions(self):
            self.assertEqual(
                operations.all_characters_in_even_positions("abcdefg"), "aceg"
            )
            self.assertEqual(
                operations.all_characters_in_even_positions("12345"), "135"
            )
            self.assertEqual(operations.all_characters_in_even_positions("A"), "A")
        def test_merge_characters_and_duplicate(self):
        # Test dla napisu "Programowanie Skryptowe"
            result = operations.merge_characters_and_duplicate("Programowanie Skryptowe")
            expected = "PwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPwPw"
            self.assertEqual(result, expected)

        # Test dla pustego napisu
            result = operations.merge_characters_and_duplicate("")
            expected = ""
            self.assertEqual(result, expected)

        # Test dla napisu z pojedynczym znakiem
            result = operations.merge_characters_and_duplicate("X")
            expected = "X"
            self.assertEqual(result, expected)

        # Test dla napisu z dwoma znakami
            result = operations.merge_characters_and_duplicate("ab")
            expected = "aaaa"
            self.assertEqual(result, expected)
            
if __name__ == "__main__":
        unittest.main()
