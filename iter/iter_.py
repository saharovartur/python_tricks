# Подкопотная работа итератора

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

# Пример реализации цикла вместо синтак.сахара for-in
repeater = Repeater('Privet')
iterator = repeater.__iter__()

while True:
    item = iterator.__next__()
    print(item)






# repeater = Repeater('Привет')
