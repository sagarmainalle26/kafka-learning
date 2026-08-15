from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    key_serializer=lambda key: str(key).encode("utf-8"),
    value_serializer=lambda value: json.dumps(value).encode('utf-8')
)


for order_id in range(2, 5):
    order = {
        "order_id": order_id,
        "customer_id": 101,
        "product_id": 100,
        "quantity": 2,
        "status": "PLACED"
    }

    producer.send(
        "orders", 
        key=order_id,
        value=order
    )

producer.flush()
producer.close()