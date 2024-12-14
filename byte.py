import dis


def hello(name):
    return f"Привет {name}"


# Примеры вывода в байткоде

# hello('Артур')
# 'Привет Артур'

# hello.__code__.co_code
# b'd\x01|\x00\x9b\x00\x9d\x02S\x00'

# hello.__code__.co_consts
# (None, 'Привет ')

# hello.__code__.co_varnames
# ('name',)


# Удобочитаемый вариант вывода через дизассемблер

# dis.dis(hello)
#   2           0 LOAD_CONST               1 ('Привет ')
#               2 LOAD_FAST                0 (name)
#               4 FORMAT_VALUE             0
#               6 BUILD_STRING             2
#               8 RETURN_VALUE
