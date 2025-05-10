# Entry point to the program and any code that doesn't fit elsewhere.

from stats import count_words
# Stats is the name of the file without the .py, and count_words is the name of the function I've imported.

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words(text))

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()