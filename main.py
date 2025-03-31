from app.io.input import input_text, read_file_builtin, read_file_pandas
from app.io.output import print_text, write_file

def main():
    text_console = input_text()
    text_builtin = read_file_builtin("data/some.txt")
    text_pandas = read_file_pandas("data/some.csv")

    print_text(text_console)
    print_text(text_builtin)
    print_text(str(text_pandas))

    write_file("data/output.txt", text_console)
    write_file("data/output.txt", text_builtin)
    write_file("data/output.txt", str(text_pandas))


if __name__ == "__main__":
    main()