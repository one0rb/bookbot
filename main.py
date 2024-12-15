def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_char_list = char_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words were found in this document.")
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times.")
    print("--- End of report ---")
    

def sort_on(dict):
    return dict["num"]


def char_dict_to_sorted_list(dict):
    sorted_list = []
    for key in dict:
        new_dict = {"char": key, "num": dict[key]}
        sorted_list.append(new_dict)
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


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