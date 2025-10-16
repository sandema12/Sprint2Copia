import os, json, pika

RABBIT_HOST = os.getenv('RABBIT_HOST')
RABBIT_USER = os.getenv('RABBIT_USER','monitoring_user')
RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD')
EXCHANGE = os.getenv('RABBIT_EXCHANGE','wms.events')

def _channel():
    credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASSWORD)
    params = pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
    conn = pika.BlockingConnection(params)
    ch = conn.channel()
    ch.exchange_declare(exchange=EXCHANGE, exchange_type='topic', durable=True)
    return conn, ch

def publish(event_key: str, payload: dict):
    conn, ch = _channel()
    ch.basic_publish(exchange=EXCHANGE, routing_key=event_key,
                     body=json.dumps(payload).encode('utf-8'))
    conn.close()
