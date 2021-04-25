# Задание 3
season_month = {"зима": (12, 1, 2), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}
month = int(input("Введите номер месяца: "))
for key in season_month.keys():
    if month in season_month[key]:
        print(f"{month}-й месяц это {key}")