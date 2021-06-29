# Задание 1
from time import sleep
from random import choice

class TrafficLight:

    __color = {"красный": 7, "желтый": 2, "зеленый": 4}


    def running(self):
        """Первый метод БЕЗ проверки порядка переключения режимов светофора"""
        for key, value in self.__color.items():
            print(key)
            sleep(value)


    def check_running(self):
        """Второй метод с проверкой порядка переключения режимов светофора"""
        a1 = choice([key for key in self.__color.keys()])
        print(a1)
        sleep(self.__color[a1])
        a2 = choice([key for key in self.__color.keys() if key != a1])
        print(a2)
        sleep(self.__color[a2])
        a3 = choice([key for key in self.__color.keys() if key != a1 and key != a2])
        print(a3)
        sleep(self.__color[a3])
        if a1 == "красный" and a2 == "желтый" and a3 == "зеленый":
            print("Светофор исправен!")
        if a1 != "красный" or a2 != "желтый" or a3 != "зеленый":
            print("Нарушен порядок переключения режимов светофора!")


svet = TrafficLight()
print("Первый метод БЕЗ проверки переключения режимов светофора:")
svet.running()
print("Второй метод с проверкой переключения режимов светофора:")
svet.check_running()