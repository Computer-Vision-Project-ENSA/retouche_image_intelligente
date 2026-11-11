"""
Module de configuration pour le projet : Retouche d'image intelligente (RDI).
Exemple de structure de configuration (TP1 - DevOps & MLOps).
"""

PROJECT_NAME = "Retouche d'image intelligente (suppression d’objet)"
JIRA_PROJECT_KEY = "RDI"

# Paramètres de prétraitement des images (Tâche Jira : RDI-20)
IMAGE_TARGET_SIZE = (512, 512)
SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg")
NORMALIZE_MEAN = (0.485, 0.456, 0.406)
NORMALIZE_STD = (0.229, 0.224, 0.225)
MASK_DILATION_KERNEL_SIZE = 5

# Paramètres des modèles ML/DL (Epic RDI-10)
SEGMENTATION_MODEL_NAME = "SAM-2"
INPAINTING_MODEL_NAME = "Stable-Diffusion-Inpainting"
FALLBACK_INPAINTING_MODEL = "LaMa"

# Métriques d'évaluation (Epic RDI-12)
SEGMENTATION_METRICS = ["IoU"]
INPAINTING_METRICS = ["PSNR", "SSIM", "LPIPS"]

