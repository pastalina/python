# Задание 5
my_list = [7, 5, 3, 3, 2]
print("Имеется рейтинг", my_list)
print("Для выхода из программы нажмите '0'")
while True:
    new_element = int(input("Введите новый элемент рейтинга: "))
    if new_element > 0:
        for el in my_list:
            if new_element == el:
                my_list.insert(my_list.index(el) + my_list.count(new_element), new_element)
                break
            elif new_element > el:
                my_list.insert(my_list.index(el), new_element)
                break
            elif new_element < min(my_list):
                my_list.insert(my_list.index(min(my_list)) + 1, new_element)
                # my_list.append(new_element)
                break
        print(my_list)
    if new_element <= 0:
        print("Программа завершена.")
        break