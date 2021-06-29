# Задание 1
out_file = open("hw5ex1", "w")
data_list = []
while True:
    data = input("Введите построчно данные (нажмите Enter еще раз, если хотите прекратить ввод): ")
    data_list.append(data + "\n")
    if data == "":
        break
out_file.writelines(data_list)
out_file.close()