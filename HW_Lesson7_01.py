import random

class Matrix:

    def __init__(self, row, col):
        self.n = row
        self.matrix = [[random.randrange(0, 10) for a in range(col)] for b in range(row)]

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix)):
                matrix = self.matrix[i][j] + other.matrix[i][j]
                print(matrix)

    def print(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])

matrix_1 = Matrix(5, 5)
matrix_2 = Matrix(5, 5)

matrix_3 = matrix_2 + matrix_2
