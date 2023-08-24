class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Order:
    def __init__(self, id):
        self.id = id
        self.items = []

    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        return total
