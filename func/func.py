# примеры работы вложенных функций
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + "..."

    def yell(text):
        return text.upper() + "!"

    if volume > 0.5:
        return yell
    else:
        return whisper


gt = get_speak_func(0.2)
print(gt("Привет"))


# Пример замыкания
def get_speak_func_2(text: object, volume: object) -> object:
    def whisper():
        return text.lower() + "..."

    def yell():
        return text.upper() + "!"

    if volume > 0.5:
        return yell
    else:
        return whisper


gp = get_speak_func_2("как дела", 0.7)
print(gp)  # или вызов сделаем так get_speak_func_2('как дела', 0.7)()


# Еще пример замыкания


def make_adder(n: object) -> object:
    def add(x: object) -> object:
        return x + n

    return add


# Пример вывода:
# plus_3 = make_adder(3)
# plus_5 = make_adder(5)
# plus_3(4)
# 7
# plus_5(10)
# 15


# Пример работы объекта как функции с помощью метода call
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


# Вывод
plus3 = Adder(3)
plus3(4)  # Вызываем объект как функцию и передаем значение

# Пример lambda функции
numbers = lambda x, y: x + y
numbers(3, 3)

(lambda x, y: x + y)(5, 3)

# Пример сортировки
tuples = [(1, "d"), (2, "b"), (4, "a"), (3, "c")]
sorted(tuples, key=lambda x: x[1])

[(4, "a"), (2, "b"), (3, "c"), (1, "d")]  # Вывод, сортировка по второму значению
