def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    print(f"this book contains {num_words} words")
    lower_case_text = to_lowercase(book_text)
    char_count(lower_case_text)

# Get the book    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

# Calculates number of words in text
def word_count(book):
    words = book.split()
    return(len(words))

# Converts text to all lower case
def to_lowercase(text):
    lowered_string = text.lower()
    return lowered_string

# Calcualtes num of times a letter occurs in a text
def char_count(x):
    dict_characters = {}
    
    for character in x:
        if character in dict_characters:
            dict_characters[character] += 1
        else:
            dict_characters[character] = 1
    
    print(dict_characters)

main()