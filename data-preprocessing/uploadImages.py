
from pathlib import Path
from google.cloud import storage
from tqdm import tqdm

# Configuration
BUCKET_NAME = "hdrplusdata"
PREFIX = "20171106_subset/"
OUTPUT_DIR = Path("../data/hdrplus")
MAX_IMAGES = 20

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Connexion anonyme à Google Cloud Storage
client = storage.Client.create_anonymous_client()
bucket = client.bucket(BUCKET_NAME)

print("Connexion à Google HDR+...")

# Lister les images finales
images = []

for blob in client.list_blobs(BUCKET_NAME, prefix=PREFIX):
    if blob.name.endswith("/final.jpg"):
        images.append(blob.name)

print(f"{len(images)} images finales trouvées.")

# Télécharger les images
for image_path in tqdm(images[:MAX_IMAGES], desc="Téléchargement"):
    parts = Path(image_path).parts
    burst_id = parts[-2]
    local_path = OUTPUT_DIR / burst_id / "final.jpg"

    local_path.parent.mkdir(parents=True, exist_ok=True)

    if local_path.exists():
        continue

    blob = bucket.blob(image_path)
    blob.download_to_filename(str(local_path))

print("Téléchargement terminé !")
