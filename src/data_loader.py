"""
Script de chargement des données pour le projet Retouche d'image intelligente.
Référence Jira : RDI-14 / RDI-20 (Collecte et préparation des données).
Exemple simplifié pour le TP1.
"""

import os
from pathlib import Path
from src.config import SUPPORTED_FORMATS


def validate_image_path(image_path: str) -> bool:
    """Vérifie si le fichier existe et possède une extension d'image supportée."""
    path = Path(image_path)
    return path.is_file() and path.suffix.lower() in SUPPORTED_FORMATS


def load_image_metadata(image_path: str) -> dict:
    """
    Exemple de fonction de chargement d'une image.
    Retourne les métadonnées de base pour le pipeline de prétraitement.
    """
    if not validate_image_path(image_path):
        raise ValueError(
            f"Fichier invalide ou format non supporté : {image_path}. "
            f"Formats acceptés : {SUPPORTED_FORMATS}"
        )

    path = Path(image_path)
    return {
        "filename": path.name,
        "path": str(path.resolve()),
        "extension": path.suffix.lower(),
        "size_bytes": os.path.getsize(path),
    }


def list_dataset_images(dataset_dir: str) -> list[str]:
    """Liste toutes les images valides présentes dans un répertoire de données (ex: COCO, Places2)."""
    root = Path(dataset_dir)
    if not root.exists():
        return []
    return [
        str(file_path)
        for file_path in root.iterdir()
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_FORMATS
    ]

