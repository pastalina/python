# Задание 5
digits_file = open("hw5ex5", "w+")
digits = input("Введите числа через пробел: ")
digits_file.write(digits)
digits_file.seek(0)
digits_list = digits_file.readline()
digits_sum = 0
for el in digits_list.split():
    digits_sum += int(el)
print("Сумма введенных чисел равна: ", digits_sum)
digits_file.close()