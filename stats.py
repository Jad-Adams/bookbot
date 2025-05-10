# contains functions for analysing the text

def count_words(text):
    split = text.split()
    num_words = len(split)
    return f"{num_words} words found in the document"