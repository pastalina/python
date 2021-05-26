# Задание 3
class OnlyInt(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        list_el = input("Вводите элементы списка. Для завершении списка введите stop: ")
        if list_el == "stop":
            break
        elif not list_el.lstrip("-+").isdigit():
            raise OnlyInt("В список вносятся только числа! Данный элемент не будет внесен в список")
        elif list_el.lstrip("-+").isdigit():
            my_list.append(int(list_el))
    except OnlyInt as err:
        print(err)
print(my_list)