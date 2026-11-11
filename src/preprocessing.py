"""
Module de prétraitement des images et des masques de segmentation.
Référence Jira : RDI-20 (Prétraitement des images) & RDI-25 (Post-traitement des masques).
Exemple simplifié pour la branche feature/image-preprocessing.
"""

from src.config import IMAGE_TARGET_SIZE, MASK_DILATION_KERNEL_SIZE


def resize_image_mock(image_shape: tuple[int, int, int], target_size: tuple[int, int] = IMAGE_TARGET_SIZE) -> dict:
    """
    Simule le redimensionnement d'une image aux dimensions attendues par SAM 2 et le modèle d'inpainting.
    """
    height, width, channels = image_shape
    return {
        "original_shape": (height, width, channels),
        "resized_shape": (target_size[0], target_size[1], channels),
        "status": "resized",
    }


def normalize_pixels(pixel_values: list[ float ]) -> list[float]:
    """
    Normalise une liste de valeurs de pixels de [0, 255] vers [0.0, 1.0].
    """
    return [round(val / 255.0, 4) for val in pixel_values]


def prepare_binary_mask(mask_values: list[int], threshold: int = 128) -> dict:
    """
    Binarise un masque de segmentation (0 = fond à conserver, 1 = objet à supprimer)
    et indique le noyau de dilatation configuré.
    """
    binary_mask = [1 if val >= threshold else 0 for val in mask_values]
    return {
        "binary_mask": binary_mask,
        "dilation_kernel": MASK_DILATION_KERNEL_SIZE,
    }

