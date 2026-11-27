FROM python:3.12-slim

WORKDIR /app

# Installer les dépendances d'abord (meilleur cache Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Utilisateur non-root
RUN useradd -m appuser
USER appuser

# Adaptez le point d'entrée à votre projet
CMD ["python", "src/app.py"]
