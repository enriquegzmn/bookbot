def main():
   text = get_book_text("books/frankenstein.txt")
   print(number_or_words(text))

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def number_or_words(text):
    words_list = text.split()
    counter = 0
    for i in words_list:
        counter += 1
    
    return f"{counter} words found in the document"
    




main()


