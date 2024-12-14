# Поиск юзера по ключу словаря

name_for_userid = {
    382: "Elis",
    980: "bob",
    590: "Dilbert",
}


def greeting(userid):
    try:
        return "Привет, %s" % name_for_userid[userid]
    except KeyError:
        return f"Ошибка! Пользователь с номером {userid} не найден"


# Еще вариант через метод get (метод словарей)
def greeting(user_id):
    return "Hello, %s " % name_for_userid.get(user_id, "Ошибка")
