def my_generator(n):
    value = 0

    while value < n:

        yield value
        value += 1


for value in my_generator(3):

    print(value)  
#-------------------------------------

squares_generator = (i * i for i in range(5))


for i in squares_generator:
    print(i)

