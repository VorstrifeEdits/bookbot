from stats import get_word_count, get_character_count, sort_on
import sys


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = get_character_count(text)
    sorted_list = sort_on(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_list.items():
        print(f"{key}: {value}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
