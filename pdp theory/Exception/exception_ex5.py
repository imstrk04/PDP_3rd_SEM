some_exceptions = [ValueError, TypeError, None, Exception]  # Add the exception types you want to raise

for choice in some_exceptions:
     try:
          print(f"\nRaising {choice}")
          if choice:
               raise choice("An error")
          else:
               print("no exception raised")
     except ValueError:
          print("Caught a ValueError")
     except TypeError:
          print("Caught a TypeError")
     except Exception as e:
          print(f"Caught some other error: {e.__class__.__name__}")
     else:
          print("This code called if there is no exception")
     finally:
          print("This cleanup code is always called")
