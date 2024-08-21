# {{ cookiecutter.project_name }}

## Installation

```bash
pip install -r requirements.txt
```

## Lancer l'application

```bash
uvicorn app.main:app --reload
```

## Base de données

Ce projet utilise {{ cookiecutter.database }} comme base de données. Configurez la connexion dans le fichier .env.