"""Module for testing input functions"""

import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import pandas as pd
from app.io.input import read_file_pandas, read_file_builtin

class TestInput(unittest.TestCase):
    """Test cases for functions read_file_builtin and read_file_builtin (input.py)"""

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

    @patch('pandas.read_csv')
    def test_read_file_pandas(self, mock_read_csv):
        """Tests read_file_pandas with a CSV"""
        mock_data = pd.DataFrame({'value1': [1, 2], 'value2': ['1', '2']})
        mock_read_csv.return_value = mock_data
        self.assertTrue(read_file_pandas('fake_path.csv').equals(mock_data))

    @patch('pandas.read_csv')
    def test_read_file_pandas_empty(self, mock_read_csv):
        """Tests read_file_pandas with an empty CSV"""
        csv_data = "Name,Age,City\nYaryna,25,Kyiv\nMaria,30,Lviv\nSvyatoslav,22,Odessa"
        mock_data = pd.read_csv(StringIO(csv_data))
        mock_read_csv.return_value = mock_data
        self.assertTrue(read_file_pandas('fake_path.csv').equals(mock_data))

    @patch('pandas.read_csv')
    def test_read_file_pandas_multiline(self, mock_read_csv):
        """Tests read_file_pandas with a multiline CSV"""
        mock_data = pd.DataFrame({'Name': ['Yaryna', 'Maria'], 'Age': [25, 30]})
        mock_read_csv.return_value = mock_data


if __name__ == '__main__':
    unittest.main()
