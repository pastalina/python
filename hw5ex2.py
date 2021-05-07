# Задание 2
poem = open("hw5ex2", "r")
poem_line = poem.readlines()
c = 0
for el in poem_line:
    c += 1
    poem_word = el.split()
    d = 0
    for elem in poem_word:
        d += 1
    print(poem_word)
    print("Количество слов в этой строке:", d)
print("Количество строк в текстовом документе:", c)
poem.close()