def main():
    book_path = "books/frankenstein.txt"
    #defines the path to the directory of books
    text = get_book_text(book_path)
    #defines the variable that stores the text retrieved from get_book_text function
    wordcount = get_word_count(text)
    print(text)
    print(wordcount)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    count = len(words)
    return(count)

main()