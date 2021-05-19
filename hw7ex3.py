# Задание 3
class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if self.cell_number - other.cell_number > 0:
            return Cell(self.cell_number - other.cell_number)
        else:
            return f"Число ячеек первой клетки меньше числа ячеек второй клетки!"

    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        return Cell(self.cell_number // other.cell_number)

    def __str__(self):
        return f"Число ячеек общей клетки: {self.cell_number}"

    def make_order(self, cell_number_in_row):
        self.cell_number_in_row = cell_number_in_row
        return "Схема клетки:\n" + ("*" * self.cell_number_in_row + "\n") * (self.cell_number // self.cell_number_in_row) + "*" * (self.cell_number % self.cell_number_in_row)


c1 = Cell(31)
c2 = Cell(18)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(10))
print(c2.make_order(6))

c1 = Cell(10)
c2 = Cell(35)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(4))
print(c2.make_order(7))