FROM node:18-alpine
WORKDIR /app
# Added this comment to trigger cache invalidation - v2
COPY . .
EXPOSE 3000
CMD ["node", "-e", "console.log('Hello from cached build v2!'); setTimeout(() => {}, 60000)"]