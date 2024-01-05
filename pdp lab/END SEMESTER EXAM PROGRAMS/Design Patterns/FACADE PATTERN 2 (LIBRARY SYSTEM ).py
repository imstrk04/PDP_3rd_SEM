# Subsystem 1
class BookCatalog:
    def __init__(self, book_name=None, author=None):
        self.book_name = book_name
        self.author = author

    # Simplified book search algorithm
    def search_book(self):
        print(f'Book found: {self.book_name} by {self.author}')


# Subsystem 2
class MemberSystem:
    def __init__(self):
        pass

    def display_member_details(self, name, mem_id):
        print(f'Member Details: Name - {name}, Member ID - {mem_id}')


# Rest of the code remains the same


# Subsystem 3
class LoanSystem:
    def __init__(self, name=None, book_name=None):
        self.name = name
        self.book_name = book_name

    def borrow_book(self):
        print(f'{self.name} has borrowed the book: {self.book_name}')


# Library Management Facade
class LibraryManagementFacade:
    def __init__(self, book_catalog, member_system, loan_system):
        self.book_catalog = book_catalog
        self.member_system = member_system
        self.loan_system = loan_system

    def enter_info(self, name, mem_id):
        self.member_system.display_member_details(name, mem_id) # if you give like this then pass the constructor and give only methods 

    def search_book(self, book_name, author):
        self.book_catalog.book_name = book_name
        self.book_catalog.author = author
        self.book_catalog.search_book()

    def borrow_book(self, name, book_name):
        self.loan_system.name = name
        self.loan_system.book_name = book_name
        self.loan_system.borrow_book()


# Driver code
book_catalog = BookCatalog()
member_system = MemberSystem()
loan_system = LoanSystem()

lib_facade = LibraryManagementFacade(book_catalog, member_system, loan_system)

# Example usage
lib_facade.enter_info("SRIHARI", "2210206")
lib_facade.search_book("discrete maths ", "veerarajan")
lib_facade.borrow_book("Srihari", "discrete maths ")
