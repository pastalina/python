# Задание 7
from math import factorial
from sys import argv

hw4ex7, n = argv


def fact(n):
    """Вычисляет факториал каждого числа в интервале от 1 до введенного числа n включительно"""
    for elem in range(1, int(n) + 1):
        yield factorial(elem)


print(fact(n))
for el in fact(n):
    print(el)