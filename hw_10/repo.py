from agregator import Order, Product

import sqlite3


class OrderRepository:
    def save_order(self, order):
        pass

    def load_order(self, order_id):
        pass

    def load_all_orders(self):
        pass


class OrderRepositoryImpl(OrderRepository):
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.create_tables()

    def create_tables(self):
        try:
            # Создание таблиц для заказов, продуктов и т.д.
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS products
                              (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                              (id INTEGER PRIMARY KEY, total REAL)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS order_items
                              (order_id INTEGER, product_id INTEGER, quantity INTEGER,
                               FOREIGN KEY (order_id) REFERENCES orders(id),
                               FOREIGN KEY (product_id) REFERENCES products(id))''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error creating tables:", e)

    def save_order(self, order):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO orders (total) VALUES (?)",
                           (order.calculate_total(),))
            order_id = cursor.lastrowid
            for item in order.items:
                cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                               (order_id, item.product.id, item.quantity))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error saving order:", e)

    def load_order(self, order_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
            order_data = cursor.fetchone()
            if not order_data:
                return None

            cursor.execute(
                "SELECT product_id, quantity FROM order_items WHERE order_id=?", (order_id,))
            items_data = cursor.fetchall()

            order = Order(order_id)
            for item_data in items_data:
                product_id, quantity = item_data
                product = self.load_product(product_id)
                if product:
                    order.add_item(product, quantity)
            return order
        except sqlite3.Error as e:
            print("Error loading order:", e)

    def load_all_orders(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id FROM orders")
            order_ids = cursor.fetchall()
            orders = []
            for order_id in order_ids:
                order = self.load_order(order_id[0])
                if order:
                    orders.append(order)
            return orders
        except sqlite3.Error as e:
            print("Error loading all orders:", e)

    def load_product(self, product_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
            product_data = cursor.fetchone()
            if not product_data:
                return None
            return Product(product_data[0], product_data[1], product_data[2])
        except sqlite3.Error as e:
            print("Error loading product:", e)
