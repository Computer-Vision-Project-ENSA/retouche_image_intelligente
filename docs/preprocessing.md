# Documentation Technique : Module de Prétraitement et Pipeline Initial

**Projet :** Retouche d'image intelligente (Suppression d'objet)  
**Clé Jira :** `RDI`  
**Branche :** `feature/image-preprocessing`  
**Tâche Jira associée :** `RDI-20` (Prétraitement des images)

---

## 1. Vue d'ensemble

Ce document décrit les composants exemples ajoutés sur la branche `feature/image-preprocessing` dans le cadre du TP1 (Mise en place d'un projet collaboratif avec Git/GitHub).

Le pipeline prépare les images avant leur passage dans les deux briques d'intelligence artificielle définies dans le cahier des charges (TP0) :
1. **Segmentation d'images (`SAM 2`) :** délimitation précise de l'objet indésirable sous forme de masque binaire.
2. **Inpainting génératif (`Stable Diffusion Inpainting` / `LaMa`) :** reconstruction réaliste de la région masquée.

---

## 2. Architecture des modules ajoutés

| Fichier | Rôle dans le projet | Référence Jira |
| :--- | :--- | :--- |
| `src/config.py` | Centralise les constantes (résolution `512x512`, formats supportés, noms des modèles, métriques `IoU`, `PSNR`, `SSIM`, `LPIPS`). | `RDI-1` / `RDI-20` |
| `src/data_loader.py` | Vérifie le format des images (`.png`, `.jpg`, `.jpeg`) et charge les métadonnées depuis les datasets (`COCO`, `Places2`, `Open Images`). | `RDI-14` |
| `src/preprocessing.py` | Implémente les fonctions de redimensionnement, de normalisation des pixels dans `[0.0, 1.0]` et de binarisation/dilatation des masques. | `RDI-20` / `RDI-25` |
| `src/model.py` | Définit la classe squelette `ObjectRemovalPipeline` articulant la segmentation par clic et l'inpainting. | `RDI-10` / `RDI-22` |

---

## 3. Étapes du prétraitement (`RDI-20`)

1. **Validation et chargement :** Vérification de l'extension et de l'intégrité du fichier image via `validate_image_path()`.
2. **Redimensionnement :** Standardisation de la résolution d'entrée à `512x512` pixels via `resize_image_mock()`.
3. **Normalisation :** Mise à l'échelle des intensités de pixels de `[0, 255]` vers `[0.0, 1.0]` via `normalize_pixels()`.
4. **Préparation du masque :** Binarisation du masque de segmentation et configuration du noyau de dilatation (`MASK_DILATION_KERNEL_SIZE = 5`) via `prepare_binary_mask()` afin d'éviter les artefacts de bordure lors de l'inpainting.

