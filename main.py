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
    
    print(alphabet_count)
    return 0

if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        book = f.read()
        f.close()
        # print_book_to_console(book)
        # print(count_words(book))
        count_letters(book)