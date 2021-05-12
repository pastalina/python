# Задание 5
class Stationery:
    def __init__(self, title):
        self.title = title
        print(f"{title}")

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка текста.")



class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка карандашных набросков.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка заголовков.")


pn = Pen("Ручка")
pn.draw()
pncl = Pencil("Карандаш")
pncl.draw()
hndl = Handle("Маркер")
hndl.draw()