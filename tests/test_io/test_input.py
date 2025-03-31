"""Module for testing input functions"""

import unittest
from unittest.mock import patch, mock_open
from app.io.input import input_text, read_file_builtin

class TestInput(unittest.TestCase):
    """Test cases for functions input_text and read_file_builtin (input.py)"""

    @patch('builtins.input', return_value='String text')
    def test_input_text(self, _mock_input):
        """Tests input_text with text input"""
        self.assertEqual(input_text(), 'String text')

    @patch('builtins.input', return_value='')
    def test_input_empty(self, _mock_input):
        """Tests input_text with empty input"""
        self.assertEqual(input_text(), '')

    @patch('builtins.input', return_value='11111111112356')
    def test_input_numbers(self, _mock_input):
        """Tests input_text with numerical input"""
        self.assertEqual(input_text(), '11111111112356')

    @patch('builtins.open', new_callable=mock_open, read_data='File text')
    def test_read_file_builtin(self, _mock_file):
        """Tests read_file_builtin with text file"""
        self.assertEqual(read_file_builtin('fake_path.txt'), 'File text')

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_read_file_builtin_empty(self, _mock_file):
        """Tests read_file_builtin with empty file"""
        self.assertEqual(read_file_builtin('fake_path.txt'), '')

    @patch('builtins.open', new_callable=mock_open,
           read_data='Kyiv\nIs the capital\nOf Great Britain')
    def test_read_file_builtin_multiline(self, _mock_file):
        """Tests read_file_builtin with multiline file"""
        self.assertEqual(read_file_builtin('fake_path.txt'),
                  'Kyiv\nIs the capital\nOf Great Britain')


if __name__ == '__main__':
    unittest.main()
