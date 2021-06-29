# Задание 1
from sys import argv

hw4ex1, productivity, wage, bonus = argv


def salary_calc(productivity, wage, bonus):
    return int(productivity) * int(wage) + int(bonus)


print(f"Выработка в часах: {productivity}")
print(f"Ставка в час: {wage}")
print(f"Премия: {bonus}")
print(f"Зарплата: {salary_calc(productivity, wage, bonus)}")