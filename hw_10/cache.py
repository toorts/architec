from cachetools import Cache, LRUCache
from repo import OrderRepository, OrderRepositoryImpl

import sqlite3

class CachedOrderRepository(OrderRepository):
    def __init__(self, database_name):
        self.database_repo = OrderRepositoryImpl(database_name)
        self.cache = LRUCache(maxsize=100)

    def load_order(self, order_id):
        cached_order = self.cache.get(order_id)
        if cached_order:
            return cached_order
        else:
            order = self.database_repo.load_order(order_id)
            if order:
                self.cache[order_id] = order
            return order

    def save_order(self, order):
        try:
            self.database_repo.save_order(order)
            self.cache[order.id] = order
        except sqlite3.Error as e:
            print("Error saving order:", e)
