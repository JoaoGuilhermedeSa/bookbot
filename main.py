def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(len(text.split()))
    char_dict = get_word_dict(text.lower()) 
    print(char_dict)
    print(report_char_dict(char_dict, len(text.split())))

def report_char_dict(char_dict, word_count):
    print("--- Begin report of books/frankenstein.txt ---") 
    print(f"{word_count} words found in the document")
    for key in char_dict:
        print(f"{key} character was found {char_dict[key]} times")
    print("--- End report ---")

def get_word_dict(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def get_book_text(path):
    with open(path) as f:
        return f.read()   



main()
