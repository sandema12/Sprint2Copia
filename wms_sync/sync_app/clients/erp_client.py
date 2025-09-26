class ERPClient:
    def send_orders(self, orders):
        for order in orders:
            print(f"ERP: sincronizando orden {order.id}")

    def send_inventory(self, inventory):
        for item in inventory:
            print(f"ERP: sincronizando inventario {item.product}")

    def send_payments(self, payments):
        for payment in payments:
            print(f"ERP: sincronizando pago {payment.id}")
