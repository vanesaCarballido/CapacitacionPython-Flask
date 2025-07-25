FROM python:3.10-slim

WORKDIR /app

# Copia todo el código al contenedor
COPY . .

# Instala Flask y Requests directamente
RUN pip install flask requests

# Expone el puerto para Flask
EXPOSE 5000

CMD ["python", "main.py"]
