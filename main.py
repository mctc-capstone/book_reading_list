""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import Book, BookError, BookStore
from menu import Menu
import ui
import traceback

store = BookStore()

def main():

    menu = create_menu()

    while True:
        try:
            choice = ui.display_menu_get_choice(menu)
            action = menu.get_action(choice)
            action()
            if choice == 'Q':
                break
        except:
            print("\nYou have this book already.\n")


def create_menu():
    """ contains menu list
     :returns: menu options"""
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    menu.add_option('7', 'Delete a book', delete_book)
    menu.add_option('8','Display the number of books', number_of_books)
    menu.add_option('Q', 'Quit', quit_program)

    return menu

def add_book():
    """ adds new book to the list and saves"""
    new_book = ui.get_book_info()
    new_book.save()

def delete_book():
    """ deletes books if in the database or displays error messages"""
    print('Which book would you like to delete?')
    while True:
        try:
            book_id=ui.get_book_id()
            book = store.get_book_by_id(book_id)
            if book is not None:
                print("Would you like to delete this book:")
                print(book)
                verification = input("y/n ")
                if verification[0].lower() == 'y':
                    book.delete()
                    break
                else:
                    print('Deletion canceled.')
                    break
            else:
                print('\nThe book ID you entered is NOT in the database. would you like to continue?\n')
                verification = input("y/n ")
                if verification[0].lower() == 'y':
                    continue
                else:
                    break
        except UnboundLocalError:
            print("Unbound Local Error has occured.","Please enter a valid ID.")
        except:
            print('An error occured.','Please enter a valid ID.')

def show_read_books():
    """ lists books that are read"""
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)

def show_unread_books():
    """ lists unread books"""
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)

def show_all_books():
    """ gets all the books in the database then displays it"""
    books = store.get_all_books()
    ui.show_books(books)

def search_book():
    """ searches book in the database then displays it"""
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    ui.show_books(matches)

def change_read():
    """ gets book if then changes it to read or unread then saves it"""
    book_id = ui.get_book_id()  #gets book id
    book = store.get_book_by_id(book_id)    #checks to see if ID in the database
    if book is not None:
        new_read = ui.get_read_value(book)  #added book so book title and author is passed when confirmed     
        book.read = new_read 
        book.save()
    else:
        print('\nThe book ID you have entered is NOT in the database\n')

def number_of_books():
    """gets all the books in the database then passes number of books """
    books = store.get_all_books() # gets all the books in the database
    ui.number_of_books(books) # pass the books number_of_books function in the ui module.

def quit_program():
    """passes message"""
    ui.message('Thank you for using this program and we hope to see you again!!')


if __name__ == '__main__':
    main()
