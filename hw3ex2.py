# Задание 2


def info_form(name, surname, birthdate, city, mail, phone):
    """Возвращает данные в одну строку"""
    print(
        f"Имя: {name}; фамилия: {surname}; день рождения: {birthdate}; город проживания: {city}; адрес электронной почты: {mail}; номер телефона: {phone}.")
    return


info_form(name="Алина", surname="Халимова", birthdate="18.02.1990", city="Москва", mail="pastalina@yandex.ru",
          phone="+79263003305")
