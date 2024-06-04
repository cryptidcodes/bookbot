def main():
    book_path = "books/frankenstein.txt"
    #defines the path to the directory of books
    text = get_book_text(book_path)
    #defines the variable that stores the text retrieved from get_book_text function
    words = text.split()
    #defines the variable that stores split strings as list of individual words
    wordcount = get_word_count(words)
    #defines the variable that stores the total word count of a given text
    charcount = get_char_count(text)
    #defines the variable that stores the total count of each unique character in a given text

    print(wordcount)
    print(charcount)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(words):
    #fn which returns word count of a string
    count = len(words)
    return(count)

def get_char_count(words):
    #fn which returns count of each unique character in a given list of strings in a dict with format char:total
    lowered_words = words.lower()
    #converts all uppercase letters to lowercase and stores them in a new variable
    charcount = {}
    #defines charcount dict
    for word in lowered_words:
        letters = word.split()
        #variable that stores a list of each character in a word
        for letter in letters:
            if letter in charcount:
                charcount[letter] += 1
            else:
                charcount[letter] = 1
    return charcount

main()