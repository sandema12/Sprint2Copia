from sync_app.models import Order, Inventory, Payment
from sync_app.clients.erp_client import ERPClient
from sync_app.clients.store_client import StoreClient

class Command(BaseCommand):
    help = 'Sincroniza datos WMS con ERP y tienda cada 0.5 segundos'

    def handle(self, *args, **kwargs):
        erp = ERPClient()
        store = StoreClient()
        self.stdout.write("Iniciando sincronización...")

        while True:
            orders = Order.objects.all()
            inventory = Inventory.objects.all()
            payments = Payment.objects.all()

            erp.send_orders(orders)
            store.send_orders(orders)
            erp.send_inventory(inventory)
            store.send_inventory(inventory)
            erp.send_payments(payments)
            store.send_payments(payments)
            time.sleep(0.5)