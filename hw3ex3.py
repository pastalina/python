# Задание 3
arg1 = int(input("Введите первое число: "))
arg2 = int(input("Введите второе число: "))
arg3 = int(input("Введите третье число: "))


def my_func(arg1, arg2, arg3):
    """Возвращает сумму двух наибольших аргументов"""
    min1 = min(arg1, arg2, arg3)
    sum_max_2 = arg1 + arg2 + arg3 - min1
    return sum_max_2


print("Сумма двух наибольших аргументов равна: ", my_func(arg1, arg2, arg3))
