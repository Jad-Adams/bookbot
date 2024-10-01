def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    
    # calculate the number of words
    num_words = word_count(book_text)
    # print(f"this book contains {num_words} words")
    
    # convert text to lowercase and count characters
    lower_case_text = to_lowercase(book_text)
    num_characters = char_count(lower_case_text)
    # print(num_characters)
    
    # print a report of how often each character occurs
    clean_report = print_report(num_characters)
    # print(clean_report)


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
    return dict_characters

def print_report(dict):
    character_report_list = []
    
    character_report_list.append(dict)

    print("character_report_list")

    
main()