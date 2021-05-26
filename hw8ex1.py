# Задание 1
class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def to_int(cls, date):
        date_list = []
        for el in date.split("-"):
            date_list.append(int(el))
        return date_list

    @staticmethod
    def valid(date):
        if 1 <= Date.to_int(date)[0] <= 31 and 1 <= Date.to_int(date)[1] <= 12 and 1900 <= Date.to_int(date)[2] <= 2021:
            pass
        else:
            if Date.to_int(date)[0] <= 1 or Date.to_int(date)[0] >= 31:
                print("Введен некорректный день месяца")
            if Date.to_int(date)[1] <= 1 or Date.to_int(date)[1] >= 12:
                print("Введен некорректный месяц")
            if Date.to_int(date)[2] <= 1900 or Date.to_int(date)[2] >= 2021:
                print("Некорректный год! Введите год в интервале 1900-2021.")


d = Date("0-34-1889")
print(d.date)
print(d.to_int("0-34-1889"))
Date.valid("0-34-1889")