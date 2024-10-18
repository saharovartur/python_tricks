#  Пример использования assert для проверки условия
def apply_discount(product, discount):
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена']
    return price


#  Пример как делать не нужно, (assert может быть отключен на уровне переменной окружения)
#  Проверка полномочий перед действием
#  Получение объекта товара
def delete_product(user, product_id):
    assert user.is_admin(), 'админ'
    assert store.has_product(product_id), 'товар'
    store.get_product(product_id).delete


#  Правильный пример проверки доступа без assert
def delete_product_ok(user, product_id):
    if not user.is_admin():
        raise AuthError('Вы не админ')
    if not store.has_product(product_id):
        raise ValueError('неизвестный товар')
    store.get_product(product_id).delete()

