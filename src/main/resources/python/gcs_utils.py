import io
import csv
from google.cloud import storage

def read_urls_from_gcs(gcs_path):
    client = storage.Client()
    bucket_name, blob_name = _split_gcs_path(gcs_path)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = blob.download_as_text()
    return [line.strip() for line in data.splitlines() if line.strip()]

def write_csv_to_gcs(rows, gcs_path, fieldnames):
    client = storage.Client()
    bucket_name, blob_name = _split_gcs_path(gcs_path)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow({k: row.get(k, "") for k in fieldnames})

    blob.upload_from_string(output.getvalue(), content_type="text/csv")

def _split_gcs_path(gcs_path):
    if not gcs_path.startswith("gs://"):
        raise ValueError(f"Not a valid GCS path: {gcs_path}")
    path = gcs_path[5:]
    parts = path.split("/", 1)
    if len(parts) != 2:
        raise ValueError(f"GCS path must be in format gs://bucket/path: {gcs_path}")
    return parts[0], parts[1]
