"""
Structure initiale du pipeline ML/DL de suppression d'objets.
Référence Jira : Epic RDI-10 (Développer le modèle IA : SAM 2 + Inpainting).
Exemple d'architecture pour le TP1 (sans chargement lourd de poids).
"""

from src.config import INPAINTING_MODEL_NAME, SEGMENTATION_MODEL_NAME


class ObjectRemovalPipeline:
    """
    Squelette du pipeline combinant :
    1. La segmentation automatique d'objet (SAM 2)
    2. La reconstruction de la zone masquée (Stable Diffusion Inpainting / LaMa)
    """

    def __init__(
        self,
        segmentation_model: str = SEGMENTATION_MODEL_NAME,
        inpainting_model: str = INPAINTING_MODEL_NAME,
    ) -> None:
        self.segmentation_model = segmentation_model
        self.inpainting_model = inpainting_model
        self.is_loaded = False

    def load_models(self) -> None:
        """Simule l'initialisation des modèles pré-entraînés."""
        self.is_loaded = True

    def segment_object(self, image_metadata: dict, click_coords: tuple[int, int]) -> dict:
        """Simule la génération d'un masque de segmentation à partir d'un clic utilisateur."""
        if not self.is_loaded:
            raise RuntimeError("Les modèles doivent être chargés avant l'inférence.")
        return {
            "model": self.segmentation_model,
            "source_image": image_metadata.get("filename"),
            "click_coords": click_coords,
            "mask_generated": True,
        }

    def inpaint_region(self, image_metadata: dict, mask_info: dict) -> dict:
        """Simule la reconstruction (inpainting) de la zone masquée."""
        if not self.is_loaded:
            raise RuntimeError("Les modèles doivent être chargés avant l'inférence.")
        return {
            "model": self.inpainting_model,
            "source_image": image_metadata.get("filename"),
            "mask_used": mask_info.get("mask_generated", False),
            "status": "inpainted_successfully",
        }

