from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

# Connexion à Elasticsearch (localhost car Docker expose sur 9200)
es = Elasticsearch("http://localhost:9200")

# Connexion au topic Kafka
consumer = KafkaConsumer(
    "stock-stream",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("🔁 Lecture Kafka démarrée, indexation dans Elasticsearch...")

# Consommation + indexation
for message in consumer:
    doc = message.value

    # Indexation dans Elasticsearch
    es.index(index="stock-stream", document=doc)
    print("✅ Document indexé :", doc)