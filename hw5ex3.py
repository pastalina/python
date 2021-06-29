# Задание 3
salary = open("hw5ex3")
salary_list = salary.readlines()
salary_sum = 0
c = 0
for el in salary_list:
    employee = el.split()
    for ind in range(len(employee)):
        if ind == 1:
            salary_size = int(employee[1])
            salary_sum += salary_size
            c += 1
            if salary_size < 20000:
                print("Сотрудник, чья зарплата меньше 20000:", employee[0])
print("Средняя величина дохода сотрудников:", salary_sum / c)
salary.close()