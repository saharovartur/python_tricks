# Пример простого декоратора


def null_decorator(func):
    return func


# Пример работы замыкания в декораторе
# Функция декоратор
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return f"Привет!"


# Пример функции декоратора с аргументами
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Трассировка: вызвана {func.__name__}()' f'c {args}, {kwargs}')

        original_result = func(*args, **kwargs)
        print(f'Трассировка: {func.__name__}()' f'вернула {original_result}')

        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'