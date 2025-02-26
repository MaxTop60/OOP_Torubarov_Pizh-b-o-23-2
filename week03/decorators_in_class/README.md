# Задание 4
## Реализуйте класс Product.
## Атрибуты экземпляра класса:
* name - название товара, строка;
* retail_price - розничная цена, число;
* purchase_price - закупочная цена, число;
## Методы:
* Свойство profit должно возвращать разницу между розничной и закупочной ценой товара.
* Статический метод average_price(), который принимает список розничных цен нескольких товаров и возвращает их среднюю розничную цену. При вызове этого метода без аргументов он должен вернуть 0.
* Свойство information должно возвращать строку с информацией о товаре (название, розничная и закупочная цена).

```PYTHON
#decorators_in_class.py
class Product:
    """
    Класс, представляющий продукт.

    Атрибуты:
        _name (str): Название продукта.
        _retail_price (int): Розничная цена продукта.
        _purchased_price (int): Закупочная цена продукта.
    """

    def __init__(self, name: str, retail_price: int, purchase_price: int):
        """
        Инициализирует объект продукта.

        Параметры:
            name (str): Название продукта.
            retail_price (int): Розничная цена продукта.
            purchase_price (int): Закупочная цена продукта.
        """
        self._name = name
        self._retail_price = retail_price
        self._purchased_price = purchase_price

    @property
    def profit(self):
        """
        Возвращает прибыль от продажи продукта.

        Возвращает:
            int: Прибыль от продажи продукта.
        """
        return self._retail_price - self._purchased_price

    @staticmethod
    def average_price(price_list: list = []):
        """
        Возвращает среднюю цену из списка цен.

        Параметры:
            price_list (list): Список цен.

        Возвращает:
            float: Средняя цена из списка цен.
        """
        if price_list == []:
            return 0
        else:
            return sum(price_list) / len(price_list)

    @property
    def information(self):
        """
        Возвращает информацию о продукте.

        Возвращает:
            str: Информация о продукте.
        """
        return f"Имя: {self._name}, розничная цена: {
            self._retail_price}, закупочная цена: {self._purchased_price}"
```

```PYTHON
from decorators_in_class import Product


def test_product_initialization():
    product = Product("Test Product", 100, 50)
    assert product._name == "Test Product"
    assert product._retail_price == 100
    assert product._purchased_price == 50


def test_product_profit():
    product = Product("Test Product", 100, 50)
    assert product.profit == 50


def test_average_price():
    assert Product.average_price([]) == 0
    assert Product.average_price([100, 200, 300]) == 200


def test_information():
    product = Product("Test Product", 100, 50)
    assert (
        product.information
        == "Имя: Test Product, розничная цена: 100, закупочная цена: 50"
    )
```