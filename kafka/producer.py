import json
import time
from kafka import KafkaProducer

# Charger les données JSON
with open("../data/stock_data_sample.json") as f:
    stock_data = json.load(f)

# Configurer le producteur Kafka
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Envoyer chaque ligne vers Kafka avec pause de 1 seconde
for record in stock_data:
    producer.send("stock-stream", value=record)
    print("✅ Message envoyé :", record["timestamp"])
    time.sleep(1)  # ⏱️ simulateur temps réel

producer.flush()
producer.close()