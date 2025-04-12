# FROM node:20-slim
# WORKDIR /app
# COPY . .
# RUN npm install && npm run build
# EXPOSE 3000
# CMD ["npm", "run", "preview", "--", "--port", "3000", "--host"]

FROM nginx:alpine
COPY . /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf