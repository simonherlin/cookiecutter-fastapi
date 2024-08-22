
# {{ cookiecutter.project_name }}

## Description

Ce projet est un template pour démarrer rapidement une API construite avec FastAPI. Il inclut une architecture modulaire, une gestion de la base de données avec SQLAlchemy, des migrations avec Alembic, et une authentification par JWT. Ce template est conçu pour être extensible et adaptable à vos besoins spécifiques.

## Fonctionnalités

- **FastAPI** : Framework web rapide pour construire des APIs en Python.
- **SQLAlchemy** : ORM pour gérer les interactions avec la base de données.
- **Alembic** : Outil de gestion des migrations pour SQLAlchemy.
- **Authentification JWT** : Authentification basée sur les JSON Web Tokens (JWT).
- **Docker** : Conteneurisation de l'application pour faciliter le déploiement.
- **Structure modulaire** : Organisation du code en modules pour une meilleure maintenabilité.

## Prérequis

- **Python 3.8+**
- **Poetry ou pip** : pour la gestion des dépendances.
- **Docker** (optionnel) : pour exécuter l'application dans un conteneur.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/yourusername/{{ cookiecutter.project_slug }}.git
   cd {{ cookiecutter.project_slug }}
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurez la base de données dans le fichier `.env` :
   ```dotenv
   DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=your_secret_key_here
   ```

## Lancer l'application

1. Appliquer les migrations de la base de données :
   ```bash
   alembic upgrade head
   ```

2. Lancer l'application avec Uvicorn :
   ```bash
   uvicorn app.main:app --reload
   ```

L'API sera disponible sur [http://localhost:8000](http://localhost:8000).

## Utilisation de Docker

Vous pouvez exécuter l'application dans un conteneur Docker :

1. Construisez l'image Docker :
   ```bash
   docker build -t {{ cookiecutter.project_slug }} .
   ```

2. Lancez le conteneur :
   ```bash
   docker run -d -p 8000:8000 --env-file .env {{ cookiecutter.project_slug }}
   ```

## Tests

Pour exécuter les tests, utilisez `pytest` :
```bash
pytest
```

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request pour tout changement ou amélioration.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.


for test