def main():
    book_source = "books/frankenstein.txt"
    with open(book_source) as f:
        open_book = f.read()
        f.close()

        word_count = count_words(open_book)

        letter_count = count_letters(open_book)
        
        sorted_letter_count = dict_to_sorted_dict(letter_count)

        print(f"--- Begin report of {book_source} ---")
        print(f"{word_count} words found in the document.")
        print("")
        for letter in sorted_letter_count:
            print(f"The letter {letter} was found {sorted_letter_count[letter]} times.")
        print("--- End report ---")

def print_book_to_console(book):
    print(book)


def count_words(book):
    words = book.split()
    return len(words)


def count_letters(book):
    all_lowercase = book.lower()
    alphabet_count = {}
    a_as_num = ord("a")
    for i in range(0,26):
        alphabet_count[str(chr(a_as_num + i))] = 0
    
    for character in all_lowercase:
        if character in alphabet_count:
            alphabet_count[character] += 1
    
    return alphabet_count


def get_value_hack(given_dict):
    # Returns the first value given from a dictionary
    for i in given_dict:
        return given_dict[i]
    


def dict_to_sorted_dict(my_dict):
    my_list = []
    sorted_dict = {}
    for i in my_dict:
        my_list.append({i:my_dict[i]})
    my_list.sort(reverse=True, key=get_value_hack)
    for dict in my_list:
        sorted_dict.update(dict)

    return sorted_dict

main()