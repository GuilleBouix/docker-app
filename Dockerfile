# Parte de una imagen base de Python (slim = liviana, sin bloat)
FROM python:3.12-slim

# Define la carpeta de trabajo dentro del contenedor
WORKDIR /code

#Copia el archivo al contenedor
COPY requirements.txt .

# Instala las dependencias dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu código
COPY ./app ./app

# El comando que se ejecuta cuando arranca el contenedor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]