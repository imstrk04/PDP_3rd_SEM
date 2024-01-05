def average(*args):
    if not args:
        return 0
    total = sum(args)
    return total / len(args)

numbers = [75, 80, 90, 95]
avg = average(*numbers)
print(f"Average of numbers: {avg}") 