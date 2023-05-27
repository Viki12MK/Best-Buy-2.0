import pytest
from products import NonStockedProduct


def test_create_non_stocked_product():
    product = NonStockedProduct("Windows License", 125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.quantity == 0
    assert product.active is True


def test_show_non_stocked_products():
    product = NonStockedProduct("Windows License", 125)
    assert product.show() == "Product: Windows License, Price: 125, Non-Stocked"

