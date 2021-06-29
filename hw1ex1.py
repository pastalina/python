# Задание 1
my_name = "Алина"
my_age = 31
my_weight = 53.5
my_story = True
my_form1 = ["Алина", 31, 53.5, True]
my_form2 = ("Алина", 31, 53.5, True)
my_form3 = {"Алина", 31, 53.5, True}
print(type(my_name))
print(type(my_age))
print(type(my_weight))
print(type(my_story))
print(type(my_form1))
print(type(my_form2))
print(type(my_form3))
name = input("Введите Ваше имя: ")
age = int(input("Введите Ваш возраст: "))
weight = float(input("Введите Ваш вес: "))
print("Меня зовут", name, ", мой возраст -", age, ", мой вес", weight, "кг.")