# Suppression Intelligente d'Objets : Segmentation et Inpainting

Ce projet académique de Computer Vision consiste à développer une application permettant de supprimer un objet indésirable d'une photo de manière transparente en combinant des techniques de segmentation et de reconstruction d'images (inpainting).

---

## Présentation du Projet

L'objectif est d'effacer des éléments non désirés sur des photos fixes en deux étapes principales :

1. **Segmentation :** Obtenir un masque binaire précis de l'objet sélectionné.
2. **Inpainting :** Reconstruire la zone masquée pour qu'elle s'intègre naturellement dans le décor.

Le projet s'appuie sur des modèles pré-entraînés pour privilégier la compréhension, l'intégration et l'évaluation rigoureuse des performances, sans passer par un entraînement lourd de modèles *from scratch*.

---

## Objectifs & Périmètre

### Inclus dans le projet :

* Photos fixes (un objet à la fois, sélection par clic).
* Interface web simple.
* Comparaison visuelle avant/après et téléchargement des résultats.

### Exclus :

* Traitement vidéo.
* Entraînement de modèles *from scratch*.
* MLOps complet (CI/CD, monitoring, cloud) et gestion d'utilisateurs.

---

## Choix Techniques

* **Segmentation :** SAM (version ViT-B) pour un masque précis à partir d'un simple clic.
* **Inpainting :** LaMa (rapide et performant pour la suppression d'objets) ; OpenCV (Telea) comme baseline simple ; Stable Diffusion Inpainting envisagé en option pour les grandes zones si le temps le permet.
* **Langage & Bibliothèques :** Python, PyTorch, OpenCV.
* **Interface Web :** Gradio ou Streamlit.
* **Environnement d'exécution :** Google Colab ou Kaggle (GPU gratuit de 6 à 8 Go de VRAM recommandé).

---

## Équipe du Projet

* **Membres de l'équipe :**
  * MADIH Mohamed Nizar
  * AZEROUAL Abderrahim
  * KOULA Amine
  * HARTI Ilyas
