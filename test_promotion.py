import unittest
from products import Product
from promotion import PercentageDiscountPromotion, SecondItemHalfPricePromotion, Buy2Get1FreePromotion


class PromotionTest(unittest.TestCase):
    def setUp(self):
        self.product = Product("Test Product", 10, 5)

    def test_percentage_discount_promotion(self):
        promotion = PercentageDiscountPromotion(20)
        discounted_price = promotion.apply_promotion(self.product, 3)
        self.assertEqual(discounted_price, 24.0)

    def test_second_item_half_price_promotion(self):
        promotion = SecondItemHalfPricePromotion()
        discounted_price = promotion.apply_promotion(self.product, 4)
        self.assertEqual(discounted_price, 30.0)

    def test_buy_get_1_free_promotion(self):
        promotion = Buy2Get1FreePromotion()
        discounted_price = promotion.apply_promotion(self.product, 5)
        self.assertEqual(discounted_price, 40.0)


if __name__ == "__main__":
    unittest.main()
