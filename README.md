## Book Reading List

Basic python book reading list application. For practicing teamwork and GitHub collaboration.

Requires Python 3.7.

### Functionality
This application is run via main.py and displays a basic UI in the terminal used to run the application. It allows the user to add, search for and show books. Each book entry also has a "read" or "unread" attribute that the user can set/use in their search. The options available to the user are listed and explained in more detail below.

#### Add Book
This option creates a new book object via ui.py's get_book_info() function. A title and author are asked of the user and saved to the book object.
 
#### Search For books
This option asks the user for a search term and creates a list of book objects via bookstore.book_search() and shows that list with ui.show_books().

#### Show Unread Books
This option creates a list of unread_books via bookstore.get_books_by_read_value() and displays that list with ui.show_books()

#### Show Read Books
This is implemented in the same way as the option above but with bookstore's get_books_by_read_value() function.

#### Show All Books
Implemented like the two options above this, but creates a list with bookstore.get_all_books()

#### Change Book Read Status
This option asks the user for a book's id via ui.get_book_info() and then asks them to enter 'read' or 'not read'. These two inputs are then used as arguments for bookstore.set_book_read().

