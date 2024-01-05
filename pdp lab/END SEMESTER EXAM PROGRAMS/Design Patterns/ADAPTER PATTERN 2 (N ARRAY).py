#target
class flatarray:

    def __init__(self, size):
        self.size = size
        self.array = [0] * self.size

    def set_value(self, index, value):
        self.array[index] = value

    def get_value(self, index):
        return self.array[index]

#adaptee
class multiarray:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.array = [[0] * columns for _ in range(rows)]

    def set_value(self, row, column, value):
        self.array[row][column] = value

    def get_value(self, row, column):
        return self.array[row][column]


#adapter
class arrayadapter(flatarray): #it inherits the target class

    def __init__(self, multi_array):
        size = multi_array.rows * multi_array.columns
        super().__init__(size)
        self.multi_array = multi_array

    #executing the target flat array with multidimensional array
    def set_value(self, index, value):
        row = index // self.multi_array.columns
        column = index % self.multi_array.columns
        self.multi_array.set_value(row, column, value)

    def get_value(self, index):
        row = index // self.multi_array.columns
        column = index % self.multi_array.columns
        return self.multi_array.get_value(row, column)

# Test the code
multi_array = multiarray(rows=3, columns=3)
adapter = arrayadapter(multi_array)

adapter.set_value(5, 100)
print(adapter.get_value(5))


    
