import pytest
from products import Product


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

