def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    get_book_text("/home/enriqueguzman/Documents/Workspace/bootdev/bookbot/books/frankenstein.txt")


