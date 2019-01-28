from dataclasses import dataclass, field

# TODO add a docstring for this module.

#method to get the counter information
def gen_id():
    return Counter.get_counter()

#class to hold counter information
class Counter:
    # TODO add a docstring for this class to explain it's purpose

    _counter = 0
    #get counter method
    @staticmethod
    def get_counter():
        Counter._counter += 1
        return Counter._counter

    #reset counter method
    @staticmethod
    def reset_counter():
        Counter._counter = 0


#class to hold book information
@dataclass
class Book:

    # TODO add a docstring for this class to explain it's purpose

    id: int = field(default_factory=gen_id, init=False)
    title: str
    author: str
    read: bool = False

    #toString method used to display the book information
    def __str__(self):
        read_status = 'have' if self.read else 'have not'
        return f'ID {self.id}, Title: {self.title}, Author: {self.author}. You {read_status} read this book.'
