"""
Objective:  Create a simple Python program that manages a collection of books. Your program will allow users to add books to a collection, list all books, and search for a book by title. This assignment will help you practice variables, lists, dictionaries, functions, loops, and user inputs.


 Requirements:


# 1.  Book Collection:  Use a list to store book information. Each book should be a dictionary with keys for `title` and `author`.


# 2.  Adding Books:  Implement a function `add_book()` that asks the user for a book title and author, creates a dictionary with this information, and adds it to the collection. Use input prompts to get user data.


# 3.  Listing Books:  Implement a function `list_books()` that prints all books in the collection, showing the title and author of each book.


# 4.  Searching Books:  Implement a function `search_books()` that asks the user for a book title, searches the collection, and prints the details of the books that match the search query. If no books are found, it should print "No books found."


5.  Main Loop:  Implement a loop that continuously asks the user what they want to do: add a book, list all books, search for a book, or quit. Use the input function to get the user's choice and call the appropriate function based on their choice.


 Hints:


- Use a list to store your books, where each book is a dictionary.

- For the main loop, you can use a while loop that runs until the user decides to quit by entering a specific command, like "quit".

- Remember to check for case sensitivity when searching for books. You might want to convert strings to lower or upper case for comparison.


 Example Output:


```

What would you like to do?

- Add a book (add)

- List all books (list)

- Search for a book (search)

- Quit (quit)

Choice: add

Enter book title: Python Basics

Enter book author: John Doe

Book added!


Choice: list

Books:

1. Title: Python Basics, Author: John Doe


Choice: search

Enter book title to search: python basics

Search Results:

1. Title: Python Basics, Author: John Doe


Choice: quit

Goodbye!

```


 Submission:  Submit your Python script file (.py) that fulfills the above requirements. Ensure your code is well-commented, explaining the functionality of each section.
"""