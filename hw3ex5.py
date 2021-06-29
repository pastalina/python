# Задание 5


def dig_sum(*args):
    """Возвращает сумму неопределенного количества аргументов"""
    return sum(args)


dig_list_2 = []
while True:
    try:
        dig_string = input("Введите числа в одну строку, разделяя пробелом (для выхода из программы нажмите 'q'): ")
        if dig_string == "q":
            break
        if "q" in dig_string:
            dig_string_q = dig_string[0:dig_string.find("q")]
            dig_list_q = [int(x) for x in dig_string_q.split()]
            print("Сумма всех чисел строки, введенных до 'q', равна:", dig_sum(*dig_list_2, *dig_list_q))
            break
        else:
            dig_list = [int(x) for x in dig_string.split()]
            print("Сумма всех чисел строки равна:", dig_sum(*dig_list, *dig_list_2))
            dig_list_2.extend(dig_list)
            continue
    except ValueError:
        print("Вы ввели недопустимые значения! Введите строку из чисел!")