# Задание 2
class ZeroDivErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(a, b):
    return a / b


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise ZeroDivErr("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели некорректное число!")
except ZeroDivErr as err:
    print(err)
else:
    print(f"a / b = {division(a, b)}")