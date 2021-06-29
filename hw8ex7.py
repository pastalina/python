# Задание 7
class ComplexNumber:
    def __init__(self, a, b):
        self.number = complex(int(a), int(b))

    def __add__(self, other):
        return f"Сумма комплексных чисел равна: {self.number + other.number}"

    def __mul__(self, other):
        return f"Произведение комплексных чисел равно: {self.number * other.number}"


cn1 = ComplexNumber(4, 3)
cn2 = ComplexNumber(2, 10)
print(cn1 + cn2)
print(cn1 * cn2)