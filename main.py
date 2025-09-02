from stats import number_or_words

def main():
   text = get_book_text("books/frankenstein.txt")
   print(number_or_words(text))

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents





main()


