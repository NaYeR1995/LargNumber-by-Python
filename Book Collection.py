import sys

# Here i defined the main Fn that have a 4 Choice operations and don't Exist until the User Choice Quit


def main():

    while True:
        print("What would you like to do?")
        print("- Add a book (add)")
        print("- List all books (list)")
        print("- Search for a book (search)")
        print("- Quit (quit)")

# i Used If statement to select the Chosen operation depended on the User Input
        operation = input("Choice: ").lower()

        if (operation == "add" or operation == 'a'):
            add_book()
            print("Book added!")
        elif (operation == "list" or operation == 'l'):
            print("Books: ")
            list_books()
        elif (operation == "search" or operation == 's'):
            search_books()
        elif (operation == "quit" or operation == 'q'):
            print("Goodbye!")
            sys.exit()


BookCollection = []

# this Fn add to BookCollection [list of objects] the New Book Info.


def add_book():
    author = input('Pleas enter the Book author: ')
    title = input('Pleas enter the Book title: ')
    newBook = {"author": author, "title": title}
    return BookCollection.append(newBook)

# this Fn list to me all Book Info on BookCollection [list of objects]


def list_books():
    count = 1
    for book in BookCollection:
        BookTitle = book["title"]
        BookAuthor = book["author"]
        bookInfo = (('{count}. Title: {BookTitle}, Author: {BookAuthor}').format(
            count=count, BookTitle=BookTitle, BookAuthor=BookAuthor))
        print(bookInfo)
        count += 1

# this Fn find to me specific Book depend on it's Title and show all Info about it from BookCollection [list of objects]
def search_books():
    BookTitle = input("What is the Title Of Book? ").lower()
    for book in BookCollection:
        if (BookTitle == book["title"].lower()):
            BookAuthor = book["author"]
            bookInfo = (('1. Title: {BookTitle}, Author: {BookAuthor}').format(BookTitle=BookTitle, BookAuthor=BookAuthor))
            print(bookInfo)
        else:
            print("This Book did not Exist, Pleas try again")


main()
