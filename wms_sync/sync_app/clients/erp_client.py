# sync_app/clients/erp_client.py

class ERPClient:
    def __init__(self):
        print("ERPClient initialized")

    def send_orders(self, orders):
        print(f"Sending orders to ERP: {orders}")
        return True

    def send_inventory(self, inventory):
        print(f"Sending inventory to ERP: {inventory}")
        return True

    def send_payments(self, payments):
        print(f"Sending payments to ERP: {payments}")
        return True
