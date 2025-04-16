
def get_book_text(path):
    with open (path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()

        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(char_dict):
    return char_dict["count"]

def char_sort(char_dict):
    result = []
    for char, count in char_dict.items():
        if char.isalpha():
             result.append({"character": char, "count": count})

    result.sort(reverse=True, key=sort_on)
    return result

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = word_count(text)
    char_stats = character_count(text)
    
main()
