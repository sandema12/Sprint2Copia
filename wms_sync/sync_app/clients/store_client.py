# sync_app/clients/store_client.py

class StoreClient:
    def __init__(self):
        print("StoreClient initialized")

    def send_orders(self, orders):
        print(f"Sending orders to Store: {orders}")
        return True

    def send_inventory(self, inventory):
        print(f"Sending inventory to Store: {inventory}")
        return True

    def send_payments(self, payments):
        print(f"Sending payments to Store: {payments}")
        return True
