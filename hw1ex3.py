# Задание 3
n = int(input("Введите число n от 1 до 9: "))
if 0 < n < 10:
    s = 3 * n + 20 * n + 100 * n
    print("n + nn + nnn = ", s)
else:
    print("Вы ввели недопустимое значение n")