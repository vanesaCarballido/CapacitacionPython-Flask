
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000



CMD ["python", "HoroscopoPokemon.py"] direccion
#preguntar si está bien