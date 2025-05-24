# 📈 Real-Time Stock Data Pipeline 

Ce projet vise à construire une architecture de traitement **temps réel** pour l’analyse de données boursières, combinant **streaming Kafka**, **indexation Elasticsearch**, **visualisation Kibana**, et **modélisation ML avec BigQuery sur GCP**.

---

## 🎯 Objectif

- Collecter en temps réel des **flux de données boursières simulées**
- Les **consommer et indexer** dans Elasticsearch pour la visualisation immédiate
- Les **stocker dans Google Cloud Storage** pour des traitements batch/ML
- Entraîner des **modèles de prédiction supervisée** (régression linéaire, séries temporelles)
- Construire un **dashboard Kibana interactif**

---

## 🧱 Architecture technique
producer.py ───▶ Kafka ───▶ consumer_to_elasticsearch.py ──▶ Elasticsearch
│
▼
Google Cloud Storage
│
▼
BigQuery ML Models

---

## 🗂 Structure du projet

Real_time_stock_pipeline/
├── kafka/
│   ├── producer.py                    # Envoie les messages JSON dans Kafka
│   ├── consumer.py                    # Consumer simple (debug terminal)
│   └── consumer_to_elasticsearch.py   # Consomme Kafka → indexe dans Elasticsearch
│
├── data/
│   ├── stock_data_sample.json         # Données simulées envoyées dans Kafka
│   └── README.md                      # Instructions pour log_inf.csv
│
├── elasticsearch_kibana/
│   └── mapping_stock_stream.json      # Mapping personnalisé pour Elasticsearch
│
├── gcp_bigquery/
│   ├── upload_to_gcs.py                            # Upload JSON vers GCS
│   ├── create_external_table.sql                   # Table externe BigQuery
│   ├── train_price_regression_model.sql            # Régression linéaire
│   ├── predict_price.sql                           # Prédiction du last_price
│   ├── train_and_predict_timeseries.sql            # Modèle ARIMA simple
│   └── train_and_predict_timeseries_multiseries.sql # ARIMA multi-instruments
│
├── docker-compose.yml                # Conteneurisation de Kafka, ES, Kibana
└── README.md                         # Documentation du projet
---

## ⚙️ Fonctionnement étape par étape

### 1. Kafka Streaming (Python)

- `producer.py` lit un fichier JSON simulé et envoie des messages sur le topic `stock-stream`
- `consumer_to_elasticsearch.py` consomme ce flux et l’indexe en direct dans Elasticsearch

### 2. Elasticsearch + Kibana

- Un **mapping personnalisé** (`mapping_stock_stream.json`) est appliqué via cURL :

```bash
curl -X PUT http://localhost:9200/_index_template/stock-stream-template \
  -H "Content-Type: application/json" \
  -d @elasticsearch_kibana/mapping_stock_stream.json 

### 3. Google Cloud Platform (GCS + BigQuery ML)

#### a. 📦 Stockage dans GCS
- Le fichier `stock_data_sample.json` est uploadé via `upload_to_gcs.py`
- Le bucket est accessible dans BigQuery

#### b. 🗃 Table externe BigQuery
- Définie dans `create_external_table.sql`
- Connectée directement au fichier JSON sur GCS

#### c. 🧠 Modélisation ML

✅ **Régression linéaire** :
- `train_price_regression_model.sql` crée un modèle supervisé pour prédire `last_price`
- `predict_price.sql` génère des prédictions

✅ **Séries temporelles (ARIMA)** :
- `train_and_predict_timeseries.sql` : prédiction simple basée sur `timestamp`
- `train_and_predict_timeseries_multiseries.sql` : modèle multi-instruments (via `instrument_token`)

