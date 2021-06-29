# Задание 6
from itertools import count, cycle
from sys import argv

hw4ex6, digit_from, digit_to, stop_list = argv


def generated_digits(digit_from, digit_to):
    """Выводит по порядку список целых чисел, начиная и заканчивая указанными числами"""
    print(f"Список целых чисел, начинающийся с {digit_from} и заканчивающийся {digit_to}:")
    for el in count(int(digit_from)):
        if el > int(digit_to):
            break
        print(el)


def repeat_elements():
    """Выводит по порядку элементы заданного списка столько раз, сколько указано"""
    c = 1
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    for el in cycle(my_list):
        if c > int(stop_list):
            break
        print(el)
        c += 1


g = generated_digits(digit_from, digit_to)
r = repeat_elements()