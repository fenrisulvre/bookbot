def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words():
    book_contents = get_book_text("books/Frankenstein.txt")
    words = book_contents.split()
    number = len(words)
    print(F"{number} words found in the document")

def chracter_count():
    book_contents = get_book_text("books/Frankenstein.txt")
    book_contents = book_contents.lower()
    letters = {}
    for i in book_contents:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    print(letters)








get_num_words()
chracter_count()
