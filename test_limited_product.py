import pytest
from products import LimitedProduct


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
