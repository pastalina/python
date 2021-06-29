my_string = input("Введите строку из нескольких слов: ")
words = list(my_string.split(" "))
for ind, el in enumerate(words, 1):
    print(ind, el[0:10:])