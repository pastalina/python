# Задание 4
n = int(input("Введите целое положительное число: "))
max_ciph = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_ciph:
        max_ciph = n % 10
    if n > 9:
        continue
    else:
        print("Самая большая цифра в числе -", max_ciph)
        break
