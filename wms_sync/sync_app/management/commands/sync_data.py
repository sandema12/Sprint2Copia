import time
from django.core.management.base import BaseCommand
from sync_app.models import Order, Inventory, Payment
from sync_app.clients.erp_client import ERPClient
from sync_app.clients.store_client import StoreClient

class Command(BaseCommand):
    help = 'Sincroniza datos del WMS con ERP y Store cada 0.5 segundos'

    def handle(self, *args, **kwargs):
        erp_client = ERPClient()
        store_client = StoreClient()

        while True:
            orders = list(Order.objects.values())
            inventory = list(Inventory.objects.values())
            payments = list(Payment.objects.values())

            erp_client.update_orders(orders)
            erp_client.update_inventory(inventory)
            erp_client.update_payments(payments)

            store_client.update_orders(orders)
            store_client.update_inventory(inventory)
            store_client.update_payments(payments)

            print(f'Sincronización realizada: {len(orders)} pedidos, '
                  f'{len(inventory)} inventario, {len(payments)} pagos')

            time.sleep(0.5)
