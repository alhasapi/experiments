
import random

class Matrix:
    def __init__(self, lines_num, rows_num):
        self.content = [ [0] * rows_num ] * lines_num
        self.lines = lines_num
        self.rows  = rows_num

    def get(self, i, j):
        return self.content[i][j]

    def set(self, i, j, value):
        self.content[i][j] = value

    def __getitem__(self, *a):
        i, j = a[0]
        return self.content[i][j]
        
    def __str__(self):
        fn = lambda z: ' '.join(map(str, z))
        return '\n'.join(map(fn, self.content))
    __repr__ = __str__


def extend_matrix(previous_matrix):
    new_matrix = Matrix(previous_matrix.lines + 2, previous_matrix.rows + 2)
    print new_matrix
    for i in range(previous_matrix.lines):
        for j in range(previous_matrix.rows):
            new_matrix.set(i + 1, j + 1 , previous_matrix.get(i, j))
    return new_matrix

def rd_insertion(matrix):
    def ass(i, v): matrix.content[i] = v
    [ass(i, map(lambda u: random.randint(1, 100), matrix.content[i])) for i in range(matrix.lines)]
    return matrix

class StructItem(Matrix):
    def __init__(self, lines_num, rows_num, center):
        self.center = center
        super(StructItem, self).__init__(lines_num, rows_num)

s = Matrix(10, 10)
v = rd_insertion(s)
z = extend_matrix(v)
