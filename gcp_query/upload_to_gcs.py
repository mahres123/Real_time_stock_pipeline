from google.cloud import storage
import os

# ✅ 1. Authentification GCP avec la clé de service
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_bigquery/mon-projet-cle.json"  

# ✅ 2. Paramètres GCS
bucket_name = "real-time-stock-bucket"  
destination_blob_name = "data/stock_data_sample.json"  
source_file = "data/stock_data_sample.json"  

# ✅ 3. Fonction d'upload vers GCS
def upload_blob():
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file)
    print(f"✅ Fichier {source_file} uploadé dans gs://{bucket_name}/{destination_blob_name}")

if __name__ == "__main__":
    upload_blob()
