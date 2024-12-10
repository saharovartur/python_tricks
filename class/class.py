# Тестовы класс
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


# Пример создания кастомного класса исключения
class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)  # получим ошибку с понятным для нас описанием


# Пример иерархии исключений с помощью наследования
class BaseViladationError(ValueError):
    pass


class NameTooShortError(BaseViladationError):
    pass


class Dog:
    num_legs = 4

    def __init__(self, name):
        self.name = name

