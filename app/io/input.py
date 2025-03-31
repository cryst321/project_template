"""Module for input functions"""

import pandas as pd

def input_text():
    """Allows the user to input text from the console.

    Returns:
        str: The text input by the user.
    """
    return input("Enter some text: ")


def read_file_builtin(file_path):
    """Reads the file using built-in functions.

    Args:
        file_path (str): Path of the file to be read.

    Returns:
        str: Contents of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()


def read_file_pandas(file_path):
    """Reads the content of a file using pandas library.

    Args:
        file_path (str): Path of the file to be read.

    Returns:
        pandas.DataFrame: The content of the file as a DataFrame.
    """
    return pd.read_csv(file_path)
