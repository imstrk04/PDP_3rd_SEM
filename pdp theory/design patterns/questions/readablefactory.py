from abc import ABC, abstractmethod

# Product
class Readable(ABC):

    @abstractmethod
    def tops(self):
        pass

    @abstractmethod
    def headlines(self):
        pass

    @abstractmethod
    def brief(self):
        pass

    @abstractmethod
    def show_subsidy(self):
        pass

# Concrete Product 1
class Books(Readable):

    def tops(self):
        #print("Top news of Best Selling Books!!")
        pass
    
    def headlines(self):
        #print("Headlines of the chapter: ")
        pass

    def brief(self):
        print("Brief content of Book")

    def show_subsidy(self):
        print("Subscription for Books: Rs. 100")

# Concrete Product 2
class NewsPaper(Readable):

    def tops(self):
        pass

    def headlines(self):
        print("Headlines of the News")

    def brief(self):
        pass

    def show_subsidy(self):
        print("Subscription for Newspaper: Rs. 50")

# Concrete Product 3
class Magazines(Readable):

    def tops(self):
        print("Top Stories of Magazine")

    def headlines(self):
        pass

    def brief(self):
        pass

    def show_subsidy(self):
        print("Subscription for Magazines: Rs. 75")

# Creator
class ReadableFactory:

    @abstractmethod
    def create_readable(self, readable_type):
        pass

    def show_info(self, readable_type):
        readable = self.create_readable(readable_type)
        readable.tops()
        readable.headlines()
        readable.brief()
        readable.show_subsidy()

# Concrete Creator
class HigginsBothams(ReadableFactory):

    def create_readable(self, readable_type):
        if readable_type.lower() == 'books':
            return Books()
        elif readable_type.lower() == 'newspaper':
            return NewsPaper()
        elif readable_type.lower() == 'magazines':
            return Magazines()

# Driver code
if __name__ == '__main__':
    readable_store = HigginsBothams()

    books = readable_store.create_readable("books")
    readable_store.show_info("books")
