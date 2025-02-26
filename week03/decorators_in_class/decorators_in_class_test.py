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
