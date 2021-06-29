# Задание 4
x = 0
y = 0


def my_func(x, y):
    """
    Возвращает число, возведенное в отрицательную степень
    :param x: > 0, float
    :param y: < 0, int

    :return: результат возведения x в степень y
    """
    while True:
        try:
            while x <= 0:
                x = float(input("Введите действительное положительное число x: "))
                if x <= 0:
                    print("Вы ввели недопустимые значения x и y!")
            while y >= 0:
                y = int(input("Введите целое отрицательное число y: "))
                if y >= 0:
                    print("Вы ввели недопустимые значения x и y!")
            else:
                break
        except ValueError or float(x) != str(x) or int(y) != float(y) or int(y) != str(y):
            print("Вы ввели недопустимые значения x и y!")
    # return round(x ** y, 10) -- вариант решения с использованием оператора **
    # Ниже представлен второй вариант решения без использования оператора ** через цикл
    super_res = 1
    for el in range(y, 0):
        super_res *= x
    return round(1 / super_res, 10)


print(f"Результат возведения x в степень y: {my_func(x, y)}")