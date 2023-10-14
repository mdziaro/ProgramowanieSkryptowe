import unittest
from unittest.mock import patch
import sys
from io import StringIO
from skrypt1 import display,run,descriptions

class TestDisplayFunction(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO) #przechwytuje wyjście do obiektu StringIO
    def test_display_true(self, mock_stdout):
        args = ['1', 'a', '2', 'b']
        show_index = "True"
        
        expected_output = "args[0] = 1\nargs[1] = a\nargs[2] = 2\nargs[3] = b\n"
        
        display(args, show_index) #wywołujemy funkcję i przechwutujemy do StringIO
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        
        
    @patch('sys.stdout', new_callable=StringIO)  
    def test_display_false(self, mock_stdout):
        args = ['1', 'a', '2', 'b']
        show_index = "False"
        
        expected_output = "1\na\n2\nb\n"
        
        display(args, show_index)
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)    


class TestRunFunction(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_run(self, mock_stdout):
        moves = ['f', 'l', 'x', '1', 'b', 'r']
        
        expected_output = "Zwierzak idzie do przodu\nZwierzak skręca w lewo\nZwierzak idzie do tyłu\nZwierzak skręca w prawo\n"
        
        run(moves, descriptions)
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
