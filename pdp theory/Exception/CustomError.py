class CustomError(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

def some_function(x):
    if x < 0:
        raise CustomError("Input value should be non-negative")

try:
    some_function(-5)
except CustomError as ce:
    print(f"Custom Error: {ce}")
else:
    print("No error occurred")
