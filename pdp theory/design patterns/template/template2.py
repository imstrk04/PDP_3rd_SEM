from abc import ABC, abstractmethod

# Abstract Class with Template Method
class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook()

    def base_operation1(self):
        print("AbstractClass: Base Operation 1")

    def base_operation2(self):
        print("AbstractClass: Base Operation 2")

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def hook(self):
        pass

# Concrete Class 1
class ConcreteClass1(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass1: Required Operation 1")

    def hook(self):
        print("ConcreteClass1: Hook Operation")

# Concrete Class 2
class ConcreteClass2(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass2: Required Operation 1")

    def hook(self):
        print("ConcreteClass2: Hook Operation")

# Client Code
if __name__ == "__main__":
    concrete_class_1 = ConcreteClass1()
    concrete_class_1.template_method()

    print()

    concrete_class_2 = ConcreteClass2()
    concrete_class_2.template_method()
