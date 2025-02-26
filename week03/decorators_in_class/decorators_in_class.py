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
