from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscountPromotion(Promotion):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * quantity * (1 - self.discount_percentage / 100)
        return discounted_price


class SecondItemHalfPricePromotion(Promotion):
    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        discounted_price = round(product.price * full_price_items) + (product.price * 0.5 * half_price_items)
        return discounted_price


class Buy2Get1FreePromotion(Promotion):
    def apply_promotion(self, product, quantity):
        price_per_item = product.price
        items_to_pay = quantity - (quantity // 3)
        total_price = price_per_item * items_to_pay
        return total_price
