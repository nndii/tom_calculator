FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /app

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ ./

# build app for production with minification
EXPOSE 8080
CMD ["npm", "run", "serve"]
