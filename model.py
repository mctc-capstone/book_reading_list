"""This module uses dataclasses to store information in the program"""

from dataclasses import dataclass, field


def gen_id():
    return Counter.get_counter()


class Counter:
    # TODO add a docstring for this class to explain it's purpose
    """This is used to generate the IDs(Keys)that are used as identifiers for each book """
    _counter = 0

    @staticmethod
    def get_counter():
        Counter._counter += 1
        return Counter._counter

    @staticmethod
    def reset_counter():
        Counter._counter = 0


@dataclass
class Book:

    # TODO add a docstring for this class to explain it's purpose
    """Book class for storing info about the books(title, generated ID, author, and whether the book has been read)"""
    id: int = field(default_factory=gen_id, init=False)
    title: str
    author: str
    read: bool = False

    def __str__(self):
        read_status = 'have' if self.read else 'have not'
        return f'ID {self.id}, Title: {self.title}, Author: {self.author}. You {read_status} read this book.'
