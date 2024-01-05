class Singleton:
    _instance = None  # Private class variable to store the instance

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example usage:

singleton_instance_1 = Singleton()
singleton_instance_2 = Singleton()

print(singleton_instance_1 is singleton_instance_2)  # Output: True
