import sys
from io import StringIO
import pytest
from unittest.mock import patch

from skrypt1 import display, run, descriptions


def test_display_with_show_index_true():
    args = ['1', 'a', '2', 'b']
    show_index = "True"
    
    expected_output = "args[0] = 1\nargs[1] = a\nargs[2] = 2\nargs[3] = b\n"
    
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        display(args, show_index)
        assert mock_stdout.getvalue() == expected_output


def test_display_with_show_index_false():
    args = ['1', 'a', '2', 'b']
    show_index = "False"
    
    expected_output = "1\na\n2\nb\n"
    
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        display(args, show_index)
        assert mock_stdout.getvalue() == expected_output
        

def test_run():
    moves = ['f', 'l', 'x', '1', 'b', 'r']
    
    expected_output = "Zwierzak idzie do przodu\nZwierzak skręca w lewo\nZwierzak idzie do tyłu\nZwierzak skręca w prawo\n"
    
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        run(moves, descriptions)
        assert mock_stdout.getvalue() == expected_output


if __name__ == '__main__':
    pytest.main()
