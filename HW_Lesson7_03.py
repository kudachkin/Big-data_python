class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        result = self.cells + other.cells
        print(result * '*')

    def __sub__(self, other):
        result = self.cells - other.cells
        if result < 0:
            print('Разность клеток меньше нуля, операция невозможна')
        else:
            print(result * '*')

    def __mul__(self, other):
        result = self.cells * other.cells
        print(result * '*')

    def __truediv__(self, other):
        result = self.cells // other.cells
        print(result * '*')


cell_1 = Cell(10)
cell_2 = Cell(2)

cell_3 = cell_1 * cell_2