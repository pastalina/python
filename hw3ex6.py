# Задание 6


def int_func(word):
    """Возвращает слово с заглавной буквы"""
    return word.capitalize()


phrase = input("Введите строку из слов, разделенных пробелами: ")
phrase_list = phrase.split()
for el in phrase_list:
    phrase = phrase.replace(el, int_func(el))
print(phrase)