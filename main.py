#f.read function

def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()
