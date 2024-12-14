# Подкопотная работа итератора


# Длинный вариант-реализация итератора
class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


# Короткий вариант реализации итератора
class RepeaterTwo:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


# Пример реализации цикла вместо синтак.сахара for-in
repeater = Repeater("Privet")
iterator = repeater.__iter__()

while True:
    item = iterator.__next__()
    print(item)

# repeater = Repeater('Привет')


# Пример реализации итератора для работы с циклом
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


rep = BoundedRepeater("artur", 3)
for i in rep:
    print(i)


# Цепочка итераторов
def integers():
    for i in range(1, 9):
        yield i


chain = integers()
list(chain)
# вывод [1, 2, 3, 4, 5, 6, 7, 8]


def sq(seq):
    for i in seq:
        yield i * i


chain = sq(integers())
list(chain)
# вывод [1, 4, 9, 16, 25, 36, 49, 64]
