def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    print(f"This document has {num_words} words.")
    print(char_dict)
    

def get_char_dict(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict


def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()