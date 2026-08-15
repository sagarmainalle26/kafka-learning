from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:29092',
    group_id="inventory-group"
)

for message in consumer:
    order = message.value

    order = json.loads(message.value.decode("utf-8"))


    print("================================")
    print("New Order Received")
    print(f"Order ID:    {order['order_id']}")
    print(f"Customer ID: {order['customer_id']}")
    print(f"Product ID:  {order['product_id']}")
    print(f"Quantity:    {order['quantity']}")
    print(f"Status:      {order['status']}")
    print(f"Partition:   {message.partition}")
    print(f"Offset:      {message.offset}")
    print("================================")

