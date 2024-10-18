#  Простой пример работы инструкции with
with open('doc.txt', 'w') as f:
    f.write('Запишем это сюда')

#  Что происходит внутри?
f = open('doc.txt', 'w')
try:
    f.write('Запишем это сюда')
finally:
    f.close()



#  Менеджер контекста
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
