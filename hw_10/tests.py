import unittest

from agregator import Product
from agregator import Order
from agregator import OrderItem


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.product1 = Product(1, "Book 1", 20.0)
        self.product2 = Product(2, "Book 2", 15.0)
        self.order = Order(1)

    def test_add_item(self):
        self.order.add_item(self.product1, 3)
        self.assertEqual(len(self.order.items), 1)
        self.assertEqual(self.order.items[0].product, self.product1)
        self.assertEqual(self.order.items[0].quantity, 3)

    def test_calculate_total(self):
        self.order.add_item(self.product1, 3)
        self.order.add_item(self.product2, 2)
        self.assertEqual(self.order.calculate_total(), 20.0 * 3 + 15.0 * 2)


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "Book 1", 20.0)

    def test_product_attributes(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Book 1")
        self.assertEqual(self.product.price, 20.0)


class TestOrderItem(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "Book 1", 20.0)
        self.order_item = OrderItem(self.product, 3)

    def test_order_item_attributes(self):
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.quantity, 3)


if __name__ == "__main__":
    unittest.main()
