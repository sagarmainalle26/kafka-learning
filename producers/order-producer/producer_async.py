from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    key_serializer=lambda key: str(key).encode("utf-8"),
    value_serializer=lambda value: json.dumps(value).encode('utf-8')
)

order = {
        "order_id": 1,
        "customer_id": 101,
        "product_id": 100,
        "quantity": 2,
        "status": "PLACED"
    }


future = producer.send(
    "orders", 
    key=order["order_id"],
    value=order
)

record_metadata = future.get(timeout=10)

print("Order event sent successfully!")
print(f"Topic: {record_metadata.topic}")
print(f"Partition: {record_metadata.partition}")
print(f"Offset: {record_metadata.offset}")

producer.flush()
producer.close()