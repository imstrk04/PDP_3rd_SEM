def funniest_division(divisor):
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        return ("divisor does not match")
    except ValueError:
        print("13!")
        return ("divisor doe not match")

result = funniest_division(13)
print(result)  