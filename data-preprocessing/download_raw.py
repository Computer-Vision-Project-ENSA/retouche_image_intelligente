
from pathlib import Path
from google.cloud import storage
from tqdm import tqdm

BUCKET_NAME = "hdrplusdata"
PREFIX = "20171106_subset/"
DATA_DIR = Path("../data/hdrplus")

client = storage.Client.create_anonymous_client()
bucket = client.bucket(BUCKET_NAME)

# Identifier les rafales déjà téléchargées
burst_ids = {
    folder.name
    for folder in DATA_DIR.iterdir()
    if folder.is_dir() and (folder / "final.jpg").exists()
}

print(f"{len(burst_ids)} rafales locales trouvées.")

# Rechercher les RAW correspondants dans le bucket
raw_files = {}

for blob in client.list_blobs(BUCKET_NAME, prefix=PREFIX):
    path = Path(blob.name)

    if path.name != "payload_N000.dng":
        continue

    matching_ids = set(path.parts) & burst_ids

    for burst_id in matching_ids:
        raw_files[burst_id] = blob.name

print(f"{len(raw_files)} fichiers RAW trouvés.")

# Télécharger un RAW par rafale
for burst_id, remote_path in tqdm(raw_files.items()):
    output_path = DATA_DIR / burst_id / "input.dng"

    if output_path.exists():
        print(f"Déjà téléchargé : {burst_id}")
        continue

    bucket.blob(remote_path).download_to_filename(
        str(output_path)
    )

print("Téléchargement terminé.")
