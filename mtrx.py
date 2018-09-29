from math import sqrt, pi, exp
from pprint import pprint as p
from operator import add, mul
from functools import partial

product = partial(reduce, mul)
class Matrix:
    def __init__(self, lines, rows):
        self.content = []
        for i in range(lines):
            s = []
            for j in range(rows):
                s.append(0)
            self.content.append(s)
        self.lines = lines
        self.rows  = rows
        self.size = lines * rows

    def get(self, i, j):
        return self.content[i][j]

    def set(self, i, j, value):
        self.content[i][j] = value

    def __repr__(self):
        fn = lambda line: ' '.join(map(str, line))
        return '\n'.join(map(fn, self.content))

    __str__ = __repr__

    def items(self):
        return reduce(lambda a, b: a + b, self.content)
    def prob(self, item):
        items = reduce(lambda a, b: a + b, self.content)
        return items.count(item) / float(len(items))

    def moyenne(self):
        items = list(set(reduce(lambda a, b: a + b, self.content)))
        return int(sum(map(lambda i: i * self.prob(i), items)) / self.size)

    def eqtype(self):
        items = list(set(reduce(lambda a, b: a + b, self.content)))
        moy = self.moyenne()
        fn = lambda z: (z - moy) ** 2
        return int(sqrt(sum(map(fn, items)) / float(self.lines * self.rows)))

from random import randint

def rd_insertion(matrix):
    for i in range(matrix.lines):
        for j in range(matrix.rows):
            value = randint(10, 90)
            matrix.set(i, j, value)

def extend_matrix(matrix):
    new_matrix = Matrix(matrix.lines + 2, matrix.rows + 2)
    for i in range(matrix.lines):
        for j in range(matrix.rows):
            value = matrix.get(i, j)
            new_matrix.set(i + 1, j + 1, value)
    return new_matrix

def symetric_insertion(matrix):
    for j in range(matrix.rows):
        matrix.set(0, j, matrix.get(2, j))
        matrix.set(matrix.lines - 1, j, matrix.get(matrix.lines - 3, j))

    for i in range(matrix.lines):
        matrix.set(i, 0, matrix.get(i, 2))
        matrix.set(i, matrix.rows - 1, matrix.get(i, matrix.lines - 3))


def fn(i, j):
    return [[(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)], [(i, j - 1), (i, j), (i, j + 1)],  [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]]

def mk_matrix(i, j, matrix):
    new = Matrix(3, 3)
    new.content = list(map(lambda line: list(map(lambda u: matrix.get(*u), line)), fn(i, j)))
    new.center  = matrix.get(i, j)
    return new

def center_items(old_matrix, ex_matrix):
    centers = []
    for i in range(old_matrix.lines):
        for j in range(old_matrix.rows):
            mt = mk_matrix(i + 1, j + 1, ex_matrix)
            centers.append(mt)
    return centers

def moy_matrix(c_matrixs, old_matrix):
    mt1 = Matrix(old_matrix.lines, old_matrix.rows)
    mt2 = Matrix(old_matrix.lines, old_matrix.rows)
    moys = list(map(lambda c: c.moyenne(), c_matrixs))
    eqs  = list(map(lambda c: c.eqtype(), c_matrixs))
    k = 0
    for i in range(old_matrix.lines):
        for j in range(old_matrix.rows):
            mt1.set(i, j, moys[k])
            mt2.set(i, j, eqs[k])
            k += 1
    return (mt1, mt2)

def to_matrix(items):
    s = []
    v = []
    c = 0
    for i in items:
        if c == 3:
            v, c = [], 0
            s.append(v)
        else:
            v.append(i)
        c += 1
    return s

def final_matrix(c_matrixs):
    fn  = lambda it, u: (1 / float(u.eqtype() * sqrt(2 * pi))) * f(it, u)
    f   = lambda it, u: exp(-(it - u.moyenne())/ float(2 * (u.eqtype() ** 2)))
    fn2 = lambda c: [fn(*k) for k in zip(c.items(), [c] * (c.lines * c.rows))]
    return [product(fn2(c)) for c in c_matrixs]

m = Matrix(10, 10)
rd_insertion(m)
# m.content = [[3, 4, 5], [7, 2, 8], [4, 8, 0]]
nm = extend_matrix(m)
symetric_insertion(nm)
c = center_items(m, nm)
my, eqt = moy_matrix(c, m)
fin = final_matrix(c)
