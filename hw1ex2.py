# Задание 2
time_in_sec = int(input("Введите время в секундах: "))
if time_in_sec > 0:
    hours = time_in_sec // 3600
    minutes = (time_in_sec % 3600) // 60
    seconds = (time_in_sec % 3600) % 60
    print("%02d:%02d:%02d" % (hours, minutes, seconds))
else:
    print("Вы ввели недопустимое значение")