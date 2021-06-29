# Задание 1
arg1 = int(input("Введите делимое: "))
arg2 = int(input("Введите делитель: "))


def division_func(arg1, arg2):
    """Возвращает результат деления arg1 на arg2"""
    try:
        div = arg1 / arg2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        return
    return div


my_division = division_func(arg1, arg2)
print(f"{arg1} / {arg2} = ", my_division)