def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    
    # calculate the number of words
    num_words = word_count(book_text)
    print(f"this document contains {num_words} words")
    
    # convert text to lowercase and count characters
    lower_case_text = to_lowercase(book_text)
    num_characters = char_count(lower_case_text)
    # print(num_characters)
    
    # print a report of how often each character occurs
    clean_report = print_report(num_characters)


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

# Calcualtes num of times a letter occurs in a text and stores data in a dictionary
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
    cleaned_list = {}
    
    # removes all weird characters
    for x, y in dict.items():
        if x.isalpha():
            cleaned_list[x] = y
            
    # populates a list with the characters
    for key, value in cleaned_list.items():
        character_report_list.append({"character": key, "count": value})
        
    character_report_list.sort(key=lambda x: x["count"], reverse=True)

    # prints a report of the characters and their count     
    for item in character_report_list:
        print(f"The {item['character']} character was found {item['count']} times")
    
    print("-- End report --")

    return
    
main()