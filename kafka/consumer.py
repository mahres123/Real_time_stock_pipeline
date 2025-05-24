from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'stock-stream',
    bootstrap_servers='127.0.0.1:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000
)

print("🟢 Consumer started, waiting for messages...")

for msg in consumer:
    print("📥 Message reçu :", msg.value)