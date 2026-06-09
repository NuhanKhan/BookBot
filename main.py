import sys
from typing import TypedDict
from stats import get_num_words as count_words
from stats import get_num_characters as count_characters
from stats import chars_dict_to_sorted_list as sort_characters

class CharacterCount(TypedDict):
    char: str
    num: int

def get_file_data(path):
    with open(path) as f:
        content = f.read()
        return content

def main(path):
    data = get_file_data(path)
    word_count = count_words(data)
    chars = count_characters(data)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {path}...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("------- Character Count --------")

    for item in sort_characters(chars):
        #print(item)
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")

    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


main(sys.argv[1])
