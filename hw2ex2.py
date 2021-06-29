# Задание 2
element_count = int(input("Введите количество строк в списке: "))
my_list = []
i = 0
ind = 0
while i < element_count:
    my_list.append(input("Введите значение: "))
    i +=1
print(my_list)
for elements in range(int(len(my_list) // 2)):
        my_list[ind], my_list[ind + 1] = my_list[ind + 1], my_list[ind]
        ind += 2
print(my_list)