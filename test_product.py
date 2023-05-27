import pytest
from products import Product, NonStockedProduct, LimitedProduct


def test_create_product():
    product = Product("Phone", 1000, 10)
    assert product.name == "Phone"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.active is True


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError) as e:
        Product("", 1000, 10)
    assert str(e.value) == "Sorry, the product name cannot be empty."

    with pytest.raises(ValueError) as e:
        Product("Phone", -1000, 10)
    assert str(e.value) == "Sorry, the price cannot be below zero."

    with pytest.raises(ValueError) as e:
        Product("Phone", 1000, -10)
    assert str(e.value) == "Sorry, the quantity cannot be below zero."


def test_product_quantity_deactivation():
    product = Product("Phone", 1000, 0)
    assert product.get_quantity() == 0
    assert product.is_active() is False


def test_product_purchase():
    product = Product("Phone", 1000, 10)
    total_price = product.buy(5)
    assert total_price == 5000
    assert product.get_quantity() == 5
    assert product.is_active() is True


def test_product_insufficient_quantity():
    product = Product("Phone", 1000, 10)
    with pytest.raises(Exception) as e:
        product.buy(15)
    assert str(e.value) == "Insufficient quantity available for purchase."


def test_product_deactivated():
    product = Product("Phone", 1000, 10)
    product.deactivate()
    assert product.is_active() is False


def test_create_non_stocked_product():
    product = NonStockedProduct("Windows License", 125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.quantity == 0
    assert product.active is True


def test_show_non_stocked_products():
    product = NonStockedProduct("Windows License", 125)
    assert product.show() == "Product: Windows License, Price: 125, Non-Stocked"


def test_create_limited_product():
    product = LimitedProduct("Shipping", 10, 1, 250)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 250
    assert product.maximum == 1
    assert product.active is True


def test_show_limited_products():
    product = LimitedProduct("Shipping", 10, 1, 250)
    assert(product.show() == "Product: Shipping, Price: 10, Quantity: 250, Maximum: 1")