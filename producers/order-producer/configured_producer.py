from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    key_serializer=lambda key: str(key).encode("utf-8"),
    value_serializer=lambda value: json.dumps(value).encode('utf-8'),
    batch_size=16384,
    linger_ms=10,
    compression_type="gzip",
    #buffer_memory=33554432,   buffer_memory is not supported in kafka-python above version 3.0.0
    max_in_flight_requests_per_connection=5
)


for order_id in range(100,1000):
    order = {
        "order_id": order_id,
        "customer_id": 102,
        "product_id": 101,
        "quantity": 2,
        "status": "PLACED"
    }

    producer.send(
        "orders", 
        key=order_id,
        value=order
    )
    print(f"Order {order_id} sent")

producer.flush()

metrics = producer.metrics()
print(metrics)

producer.close()

print("orders sent successfully")