import asyncio

async def print_multiplication_table():
    number = int(input("Enter a number for multiplication table: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    print("Multiplication table completed.")

async def check_prime():
    number = int(input("Enter a number to check if it's prime: "))
    is_prime = all(number % i != 0 for i in range(2, int(number**0.5) + 1))
    print(f"{number} is {'prime' if is_prime else 'not prime'}.")
    print("Prime check completed.")

async def calculate_factorial():
    number = int(input("Enter a number for factorial calculation: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Factorial of {number} is {factorial}.")
    print("Factorial calculation completed.")

async def main():
    # Run all three coroutines concurrently
    tasks = [check_prime(), print_multiplication_table(), calculate_factorial()]
    await asyncio.gather(*tasks)
    print("Successful completion.")

asyncio.run(main())