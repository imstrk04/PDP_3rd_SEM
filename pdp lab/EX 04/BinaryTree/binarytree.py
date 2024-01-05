from abc import ABC, abstractmethod

class BinaryTree(ABC):
    def __init__(self):
        self.root = None

    @abstractmethod
    def create_tree(self, iterable):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def traverse(self):
        pass
