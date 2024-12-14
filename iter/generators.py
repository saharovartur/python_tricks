# перепишем реализацию итератора
class RepeaterTwo:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


# в генератор (с вызовом бесконечного цикла)
def repeater(value):
    while True:
        yield value


# Простой генератор
def repeat_three(value):
    yield value
    yield value
    yield value


# Генератор с указанием кол-во итераций
def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value


# Пример функции генератора
def bounded_repeater_2(value, max_repeats):
    for i in range(max_repeats):
        yield value


# Пример выражения генератора, аналогичный
iterator = ("Hello" for i in range(2))

even_squares = (x * x for x in range(10) if x % 2 == 0)
# for x in even_squares:
#     print(x)

for x in ('Repo' for i in range(3)):
    print(x)
