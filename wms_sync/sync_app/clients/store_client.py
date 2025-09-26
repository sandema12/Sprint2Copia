from .base_client import BaseClient

class StoreClient(BaseClient):
    ORDERS_URL = 'http://localhost:8082/store/orders'
    INVENTORY_URL = 'http://localhost:8082/store/inventory'
    PAYMENTS_URL = 'http://localhost:8082/store/payments'

    def update_orders(self, orders):
        self.post_data(self.ORDERS_URL, orders)

    def update_inventory(self, inventory):
        self.post_data(self.INVENTORY_URL, inventory)

    def update_payments(self, payments):
        self.post_data(self.PAYMENTS_URL, payments)
