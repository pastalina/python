# Задание 4
digits = open('hw5ex4', "r")
digits_rus = open('hw5ex4_rus', "w")
for line in digits:
    if "One" in line:
        new_string = line.replace("One", "Один")
    elif "Two" in line:
        new_string = line.replace("Two", "Два")
    elif "Three" in line:
        new_string = line.replace("Three", "Три")
    elif "Four" in line:
        new_string = line.replace("Four", "Четыре")
    digits_rus.write(new_string)
digits.close()
digits_rus.close()
