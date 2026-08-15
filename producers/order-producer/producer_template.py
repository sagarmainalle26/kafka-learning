from kafka import KafkaProducer
import json


# -----------------------------
# Kafka Producer Configuration
# -----------------------------

producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    key_serializer=lambda key: str(key).encode("utf-8"),
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


# -----------------------------
# Produce Messages
# -----------------------------

for order_id in range(2, 5):

    order = {
        "order_id": order_id,
        "customer_id": 101,
        "product_id": 100,
        "quantity": 2,
        "status": "PLACED"
    }

    future = producer.send(
        topic="orders",
        key=order_id,
        value=order
    )

    # Optional: Use future.get() when synchronous sending is required
    # metadata = future.get(timeout=10)
    # print(
    #     f"Sent order {order_id} | "
    #     f"Partition: {metadata.partition} | "
    #     f"Offset: {metadata.offset}"
    # )


# -----------------------------
# Finish Producer
# -----------------------------

producer.flush()
producer.close()