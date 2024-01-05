from abc import ABC, abstractmethod

# Decorator class to modify the price of the book based on print type
class PriceModifierDecorator(ABC):
    def __init__(self, book):
        self.book = book

    @abstractmethod
    def get_price(self):
        pass

# Concrete decorator for digital print type
class DigitalPrintDecorator(PriceModifierDecorator):
    def get_price(self):
        base_price = self.book.get_price()
        return base_price + 5  # Add an extra cost for digital print

# Concrete decorator for hard copy print type
class HardCopyPrintDecorator(PriceModifierDecorator):
    def get_price(self):
        base_price = self.book.get_price()
        return base_price + 10  # Add an extra cost for hard copy print

# Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_price(self):
        return self.price

# Reader class
class Reader:
    def read_book(self, book, print_type):
        if print_type == 'digital':
            decorator = DigitalPrintDecorator(book)
        elif print_type == 'hard_copy':
            decorator = HardCopyPrintDecorator(book)
        else:
            print(f"Print type '{print_type}' is not supported. Please choose a valid print type.")
            return

        final_price = decorator.get_price()
        print(f"Reading '{book.title}' by {book.author} in {print_type} print type. Final price: ${final_price}")


# Example Usage
book = Book(title="The Python Journey", author="John Doe", price=20)
reader = Reader()

# Reader using a device that supports digital print type
reader.read_book(book, print_type='digital')

# Reader using a device that supports hard copy print type
reader.read_book(book, print_type='hard_copy')

# Reader attempting to use an unsupported print type
reader.read_book(book, print_type='invalid_print_type')
5
