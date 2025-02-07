# Utilise une image officielle de Python
FROM python:3.8-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie tout le contenu dans l'image
COPY . .

# Installe les dépendances nécessaires
RUN pip install pytest

# Définit la commande de lancement pour les tests avec pytest 
CMD ["pytest", "tests"]
