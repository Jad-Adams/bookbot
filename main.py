def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words(text))

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    split = text.split()
    num_words = len(split)
    return f"{num_words} words found in the document"

main()