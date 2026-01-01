

# 🚀 API FastAPI - Projet Démo

[![CI/CD MYFastAPI](https://github.com/Samou19/my_fastapi/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Samou19/my_fastapi/actions/workflows/ci-cd.yml)
![Docker Pulls](https://img.shields.io/docker/pulls/samou19/my-fastapi)
![Docker Image Size](https://img.shields.io/docker/image-size/samou19/my-fastapi/latest)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)


## Contexte
En Data Science, la valeur ne se limite pas aux modèles prédictifs : elle se concrétise lorsqu’ils deviennent des solutions fiables, déployées et utilisées.
Ce projet illustre ma capacité à industrialiser des solutions Data en appliquant les standards du marché.

## Objectif
Créer une API REST avec FastAPI, pensée pour être scalable et prête pour la production, tout en intégrant les bonnes pratiques MLOps et DevOps.

## Pourquoi ce projet ?
- Montrer comment industrialiser des solutions Data.
- Partager des bonnes pratiques MLOps et DevOps.
- Accompagner celles et ceux qui souhaitent monter en compétences sur FastAPI, Docker, CI/CD.

## Ce que j’ai mis en place
- Endpoints GET & POST avec validation des données via Pydantic
- Tests unitaires automatisés avec Pytest
- Pipeline CI/CD GitHub Actions : tests, build & push de l’image Docker sur DockerHub
- Déploiement cloud sur Render avec conteneurisation Docker

## Résultat
Une API simple construite avec **FastAPI**, incluant des endpoints GET et POST, la validation des données avec **Pydantic**, et un déploiement via **Docker**.
Ce projet démontre ma capacité à passer du modèle à la solution industrialisée, en respectant les standards du marché.


---

## ✅ Fonctionnalités
- Endpoint racine (`GET /`) : Retourne un message de bienvenue.
- Endpoint pour récupérer un item (`GET /items/{item_id}`).
- Endpoint pour créer un item (`POST- Endpoint pour créer un item (`POST /items/`) avec validation des données.

---

## ▶️ Installation et exécution locale
```bash
# Cloner le projet
git clone git@github.com:Samou19/my_fastapi.git
cd my_fastapi

# Créer un environnement virtuel
python -m venv env
env\Scripts\activate   # Windows
# ou source env/bin/activate (Linux/Mac)

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
uvicorn app.main:app --reload
```
## 🐳 Déploiement avec Docker
```bash
docker build -t my_fastapi:latest .
docker run
```
## ✅ Tests unitaires
```bash
pytest 
```
## 🔗 CI/CD avec GitHub Actions
- Tests automatiques avec pytest
- Build et push de l’image Docker sur DockerHub
- Artefact avec lien vers l’image Docker

## 📌 Endpoints
- GET / → Message de bienvenue
- GET /items/{item_id} → Retourne un item
- POST /items/ → Crée un item (JSON)

## 🚀 Déploiement sur Render

- Créer un compte Render : https://render.com
- Connecter ton dépôt GitHub et choisir la branche (ex. main).
- Configurer le service 
- Dockerfile requis
```bash
EXPOSE 10000
```
- Tester après déploiement : https://<nom-du-service>.onrender.com/docs



## 🛠 Technologies
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/)

## 📜 Licence
- MIT