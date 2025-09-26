from .base_client import BaseClient

class ERPClient(BaseClient):
    ORDERS_URL = 'http://localhost:8081/erp/orders'
    INVENTORY_URL = 'http://localhost:8081/erp/inventory'
    PAYMENTS_URL = 'http://localhost:8081/erp/payments'

    def update_orders(self, orders):
        self.post_data(self.ORDERS_URL, orders)

    def update_inventory(self, inventory):
        self.post_data(self.INVENTORY_URL, inventory)

    def update_payments(self, payments):
        self.post_data(self.PAYMENTS_URL, payments)
