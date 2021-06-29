# Задание 6
n = 1
x = 1
sale = []
while x < 5:
    char_1 = input("Введите название товара: ")
    char_2 = input("Введите цвет товара: ")
    char_3 = int(input("Введите цену товара: "))
    char_4 = int(input("Введите размер товара: "))
    char_5 = int(input("Введите количество товара: "))
    market = {"название": char_1, "цвет": char_2, "цена": char_3, "размер": char_4, "количество": char_5}
    goods = (n, market)
    sale.append(goods)
    n += 1
    x += 1
print(sale)
list_char_1 = []
list_char_name = []
list_char_color = []
list_char_price = []
list_char_size = []
list_char_count = []
for el in sale:
    for elem in el:
        list_char_1.append(elem)
b = 0
for element in list_char_1:
    list_char_1.pop(b)
    b += 1
for dicts in list_char_1:
    list_char_name.append(dicts.get("название"))
    list_char_color.append(dicts.get("цвет"))
    list_char_price.append(dicts.get("цена"))
    list_char_size.append(dicts.get("размер"))
    list_char_count.append(dicts.get("количество"))
print('"название": ', list_char_name)
print('"цвет": ', list_char_color)
print('"цена": ', list_char_price)
print('"размер": ', list_char_size)
print('"количество": ', list_char_count)