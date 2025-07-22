FROM node:18-alpine
WORKDIR /app
COPY . .
EXPOSE 3000
CMD ["node", "-e", "console.log('Hello from cached build!'); setTimeout(() => {}, 60000)"]