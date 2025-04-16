from stats import word_count, character_count, get_book_text, char_sort

import sys

def run_program():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    text = get_book_text(path_to_file)

    char_dict = character_count(text)

   # sorted_chars = char_sort(char_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")  # You may need to adjust based on your actual `char_dict`.
    print("--------- Character Count -------")

    for char_data in char_sort(char_dict):
        if char_data["character"].isalpha():  # Include only alphabetical characters
            print(f"{char_data['character']}: {char_data['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    run_program()
