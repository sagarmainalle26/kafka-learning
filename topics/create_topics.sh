#!/bin/bash

docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic orders \
  --partitions 3 \
  --replication-factor 1 \
  --bootstrap-server localhost:9092

docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic customers \
  --partitions 3 \
  --replication-factor 1 \
  --bootstrap-server localhost:9092

docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic payments \
  --partitions 3 \
  --replication-factor 1 \
  --bootstrap-server localhost:9092

docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic inventory \
  --partitions 3 \
  --replication-factor 1 \
  --bootstrap-server localhost:9092

docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic shipments \
  --partitions 3 \
  --replication-factor 1 \
  --bootstrap-server localhost:9092