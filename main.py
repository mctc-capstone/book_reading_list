""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import BookStore
from menu import Menu
import ui

store = BookStore()

QUIT = 'Q'


def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == QUIT:
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    menu.add_option('7', 'Delete Book', delete_book)
    menu.add_option(QUIT, 'Quit', quit_program)

    return menu


def add_book():
    
    new_book = ui.get_book_info()
    
    print("\n") # adding blank line after list of books
    all_books = store.get_all_books()
    if new_book in all_books:
        ui.message('The book already exists')
    else:
    store.add_book(new_book)
        
    print("\n") # adding blank line after list of books
    ui.message('New book Added!')
   
    # TODO show an error message if a book is already in the store, don't add book

#method to allow user to delete a book
def delete_book():
    try:
        bookStore = BookStore()
        book = input('Enter the book ID. ')
        bookStore.delete_book()

    except ValueError:
        raise bookStore.BookError('Error: Book Not Found')

def show_read_books():
    read_books = store.get_books_by_read_value(True)
    print("\n") # adding blank line after list of books
    ui.show_books(read_books)
    print("\n") # adding blank line after list of books


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    print("\n") # adding blank line after list of books
    ui.show_books(unread_books)
    print("\n") # adding blank line after list of books


def show_all_books():
    books = store.get_all_books()
    print("\n") # adding blank line after list of books
    ui.show_books(books)
    print("\n") # adding blank line after list of books


def search_book():
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    print("\n") # adding blank line after list of books
    ui.show_books(matches)
    print("\n") # adding blank line after list of books


def change_read():

    book_id = ui.get_book_id()
    try:                               #Try statement will search the store to get the book name by its book_id
        book = store.get_book(book_id)
    except:                            # If book is not found or the book_id is incorrect etc, then the 'except' block will be executed
        ui.message('The book is not in Store!')
    else:                              #else as the book name will be retrieved from the store
                                       #it will be certain that the book exists, hence the book_read_value() will be retrieved.
        new_read = ui.get_read_value()
        store.set_book_read(book_id, new_read)
   
    # TODO show error message if book's ID is not found.


def quit_program():
    ui.message('Thanks and bye!')



if __name__ == '__main__':
    main()
