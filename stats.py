def number_or_words(text):
    words_list = text.split()
    counter = 0
    for i in words_list:
        counter += 1
    
    return f"{counter} words found in the document"