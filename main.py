def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

import sys
from stats import word_count
from stats import character_count
from stats import sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print(f"DEBUG: Using path: {path}")
    text = get_book_text(path)
    print(f"DEBUG: First 50 characters: {text[50]}")
    word_amount = word_count(text)
    character_dictionary = character_count(text)
    sorted_chars = sorted_list(character_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_amount} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")

    print("============= END ===============")        

main()
