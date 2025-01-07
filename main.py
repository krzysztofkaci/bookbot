import re
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = letter_counter(text)

    print(report(text, sorting(count), book_path))

# Returns letters lowered and counted
def letter_counter(text):
    lowered = text.lower()
    removed_special = re.sub('[^a-z]', '', lowered)
    count = {}
    for i in removed_special:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
    

# Sorting letters from highest use to lowest
def sorting(text):
    text_sorted = dict(sorted(text.items(), reverse=True, key=lambda item: item[1]))
    return text_sorted

    
def report(text, count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{countin(text)} words were found in the document\n")
    for i in count:
        print(f"The '{i}' character was found {count[i]} times")
    print(f"--- End report ---")
    return "\n"



#----------------------------------------------------#
# Count how many words are in a file
def countin(booktext):
    words = booktext.split()
    return len(words)

# Open file
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()