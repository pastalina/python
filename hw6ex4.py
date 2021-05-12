# Задание 4
class Car:
    is_police = True
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print("Машина поехала")

    def stop(self):
        if self.speed == 0:
            print("Машина остановилась")

    def turn(self, direction):
        if self.speed > 0:
            print(f"Машина поехала {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена!")
        else:
            print(f"Текущая скорость: {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена!")
        else:
            print(f"Текущая скорость: {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


tc = TownCar(60, "черный", "Mazda")
tc.go()
tc.stop()
tc.turn("направо")
tc.show_speed()
print(tc.is_police)
sc = SportCar(0, "красный", "Porsche")
sc.go()
sc.stop()
sc.turn("прямо")
sc.show_speed()
print(sc.is_police)
wc = WorkCar(50, "серый", "УАЗ")
wc.go()
wc.stop()
wc.turn("налево")
wc.show_speed()
print(wc.is_police)
pc = PoliceCar(90, "синий", "Toyota")
pc.go()
pc.stop()
pc.turn("прямо")
pc.show_speed()
print(pc.is_police)




