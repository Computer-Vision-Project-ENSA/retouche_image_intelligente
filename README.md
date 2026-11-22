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

- Photos fixes (un objet à la fois, sélection par clic).
- Interface web simple.
- Comparaison visuelle avant/après et téléchargement des résultats.
- Développement d'une API Backend pour orchestrer les modèles.
- Mise en place d'une pipeline CI/CD pour automatiser les tests et le déploiement.

### Exclus :

- Traitement vidéo.
- Entraînement de modèles *from scratch*.
- Gestion des comptes utilisateurs.

---

## Choix Techniques

- **Segmentation :** SAM (version ViT-B) pour un masque précis à partir d'un simple clic.
- **Inpainting :** LaMa (rapide et performant pour la suppression d'objets) ; OpenCV (Telea) comme baseline simple ; Stable Diffusion Inpainting envisagé en option pour les grandes zones si le temps le permet.
- **Langage & Bibliothèques :** Python, PyTorch, OpenCV.
- **Interface Web :** React, TypeScript et Vite.
- **Backend :** FastAPI.
- **Environnement d'expérimentation :** Google Colab ou Kaggle (GPU selon les ressources disponibles).
- **Conteneurisation :** Docker.
- **CI/CD :** GitHub Actions.

---

## Architecture du Projet

Le projet adopte une architecture **monorepo**, organisée en trois composants principaux : `frontend/`, `backend/` et `ml/`.

Cette organisation permet de séparer l'interface utilisateur, la logique applicative et les modèles de Computer Vision, tout en facilitant les tests automatisés et l'intégration continue.

### Structure des dossiers

```text
retouche_image_intelligente/
│
├── frontend/                   # Interface utilisateur React
│   ├── src/                    # Composants, pages et services
│   └── public/                 # Ressources statiques
│
├── backend/                    # API FastAPI
│   ├── app/
│   │   ├── api/                # Endpoints REST
│   │   ├── services/           # Orchestration des traitements
│   │   ├── schemas/            # Validation des requêtes
│   │   └── main.py             # Point d'entrée de l'API
│   └── tests/                  # Tests Backend
│
├── ml/                         # Computer Vision et Deep Learning
│   ├── segmentation/
│   │   ├── training/           # Expérimentations / fine-tuning
│   │   ├── evaluation/         # Évaluation de SAM
│   │   └── inference/          # Génération des masques
│   │
│   ├── retouching/
│   │   ├── training/           # Expérimentations / fine-tuning
│   │   ├── evaluation/         # Évaluation de l'inpainting
│   │   └── inference/          # Reconstruction des images
│   │
│   ├── common/
│   │   ├── preprocessing/      # Prétraitement des images
│   │   └── postprocessing/     # Post-traitement des résultats
│   │
│   ├── notebooks/              # Expérimentations Kaggle / Colab
│   └── tests/                  # Tests Machine Learning
│
├── .github/
│   └── workflows/
│       ├── ci.yml              # Intégration continue
│       └── cd.yml              # Déploiement continu
│
├── docs/                       # Documentation technique
├── docker-compose.yml          # Configuration Docker
├── .gitignore
└── README.md
```

### Description des composants

**Frontend — React & TypeScript**

Interface permettant à l'utilisateur d'importer une image, de sélectionner un objet par clic, de visualiser le résultat avant/après et de télécharger l'image modifiée.

**Backend — FastAPI**

API REST chargée de recevoir les images et les coordonnées de sélection, d'orchestrer les opérations de segmentation et d'inpainting, puis de retourner le résultat au Frontend.

**Machine Learning — Computer Vision**

Regroupe les modèles pré-entraînés et les fonctions nécessaires à leur utilisation :

- **Segmentation :** SAM (ViT-B) pour générer le masque de l'objet sélectionné.
- **Inpainting :** LaMa pour reconstruire la zone masquée.
- **Baseline :** OpenCV Telea pour comparer les résultats.
- **Expérimentation optionnelle :** Stable Diffusion Inpainting.

**CI/CD — GitHub Actions**

Automatisation des tests, de la validation du code, de la construction des images Docker et du déploiement de l'application.

### Pipeline de traitement

```text
Utilisateur
    │
    ▼
Frontend (React)
    │
    │ Image + Coordonnées du clic
    ▼
Backend (FastAPI)
    │
    ▼
Segmentation (SAM)
    │
    │ Masque binaire
    ▼
Inpainting (LaMa)
    │
    │ Image reconstruite
    ▼
Backend (FastAPI)
    │
    ▼
Frontend
    │
    ▼
Visualisation avant/après
et téléchargement
```

Les expérimentations et l'évaluation des modèles seront réalisées sur Kaggle ou Google Colab, en utilisant les ressources GPU disponibles.

Les modèles sélectionnés seront ensuite intégrés au système d'inférence pour le déploiement de l'application.

---

## Équipe du Projet

**Membres de l'équipe :**

- MADIH Mohamed Nizar
- AZEROUAL Abderrahim
- KOULA Amine
- HARTI Ilyas