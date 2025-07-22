FROM node:18-alpine
WORKDIR /app
# Added this comment to trigger cache invalidation - v3
# Testing :latest tag layer caching functionality
COPY . .
EXPOSE 3000
CMD ["node", "-e", "console.log('Hello from cached build v3 - testing layer cache!'); setTimeout(() => {}, 60000)"]