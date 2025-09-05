import sys

from stats import get_num_words
from stats import get_stats
from stats import get_sorted_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    total_words = get_num_words(file_contents)
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    stats = get_stats(file_contents)
    sorted_stats = get_sorted_dictionary(stats)
    for stat in sorted_stats:
        if stat["char"].isalpha():
            print(f"{stat["char"]}: {stat["num"]}")
    print("============= END ===============")
            

main()
