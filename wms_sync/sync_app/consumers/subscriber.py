import os, json, pika, django
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wms_sync.settings')
django.setup()

from sync_app.clients.erp_client import ERPClient
from sync_app.clients.store_client import StoreClient

RABBIT_HOST = os.getenv('RABBIT_HOST')
RABBIT_USER = os.getenv('RABBIT_USER','monitoring_user')
RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD')
EXCHANGE = os.getenv('RABBIT_EXCHANGE','wms.events')
QUEUE = os.getenv('QUEUE_NAME','wms-sync')
BINDINGS = os.getenv('BINDING_KEYS','orders.* inventory.updated payments.confirmed').split()

erp, store = ERPClient(), StoreClient()

def on_message(ch, method, properties, body):
    event = method.routing_key
    data = json.loads(body.decode('utf-8'))
    print(f"[x] {event} {data}")

    if event.startswith('orders.'):
        erp.send_orders([data]); store.send_orders([data])
    elif event == 'inventory.updated':
        erp.send_inventory([data]); store.send_inventory([data])
    elif event == 'payments.confirmed':
        erp.send_payments([data])

    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASSWORD)
    params = pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic', durable=True)
    channel.queue_declare(queue=QUEUE, durable=True)
    for key in BINDINGS:
        channel.queue_bind(exchange=EXCHANGE, queue=QUEUE, routing_key=key)
    channel.basic_qos(prefetch_count=50)
    channel.basic_consume(queue=QUEUE, on_message_callback=on_message)
    print("[*] Waiting for messages ...")
    channel.start_consuming()

if __name__ == "__main__":
    main()
