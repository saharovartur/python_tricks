
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
        raise NameTooShortError(name) # получим ошибку с понятным для нас описанием
