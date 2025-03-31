"""Module for output functions"""

def print_text(text):
    """Prints given text to the console.

    Args:
        text (str): Text to print to the console.

    Returns:
        None
    """
    print(text)

def write_file(file_path, text):
    """Writes given text to the file.

    Args:
            file_path (str): Path to the file.
            text (str): Text to write to the file.

        Returns:
            None
        """
    with open(file_path,"a") as file:
        file.write(text + "\n")
