def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_contents = get_book_text("books/Frankenstein.txt")
    words = book_contents.split()
    
       
    number = len(words)
    print(F"{number} words found in the document")

main()