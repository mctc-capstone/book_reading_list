from unittest import TestCase
import os 

import bookstore
from bookstore import Book, BookStore


class TestBook(TestCase):

    @classmethod
    def setUpClass(cls):
        bookstore.db = os.path.join('database', 'test_books.db')
        BookStore.instance = None 

    def setUp(self):
        self.store = BookStore()
        self.store.delete_all_books()


    def test_create_book_default_unread(self):
        bk = Book('Title', 'Author')
        self.assertFalse(bk.read)


    def test_string(self):
        bk = Book('AAAA', 'BBBB', True)
        self.assertIn('AAAA', str(bk))
        self.assertIn('BBBB', str(bk))
        self.assertIn('You have read', str(bk))


    def test_save_add_to_db(self):
        bk = Book('AAA', 'BBB', True)
        bk.save()
        self.assertIsNotNone(bk.id)  # Check book has ID
        self.assertEqual(bk, self.store.get_book_by_id(bk.id))
        self.assertTrue(self.store.exact_match(bk))
        

    def test_save_update_changes_to_db(self):
        bk = Book('CCC', 'DDD', True)
        bk.save()
        
        # Change some attributes and save 
        bk.author = 'EEE'
        bk.title = 'FFF'
        bk.read = False 

        bk.save() 
        
        # Check DB has same data as bk Book object 
        self.assertEqual(bk, self.store.get_book_by_id(bk.id))
        self.assertTrue(bk, self.store.exact_match(bk))
        

    def test_delete_book_removes_from_database(self):
        bk_1 = Book('GGG', 'HHH', True)
        bk_2 = Book('III', 'JJJ', False)
        bk_1.save()
        bk_2.save()

        bk_1.delete()
        self.assertEqual(1, self.store.book_count())

        bk_2.delete()
        self.assertEqual(0, self.store.book_count())


    def test_delete_unsaved_book_error(self):
        self.fail('Finish this test')
        # TODO
        # Create a new Book object, but don't save it
        # Call the Book object's delete method 
        # Expect a BookError to be raised, since the Book object won't have an ID that can be found in the database 

