def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"this book contains {num_words} words")
    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = book.split()
    return(len(words))

main()