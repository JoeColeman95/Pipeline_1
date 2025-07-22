FROM node:18-alpine
WORKDIR /app
# Added this comment to trigger cache invalidation - v4
# Testing :latest tag layer caching functionality - another test
RUN echo "Installing dependencies..." && npm install -g nodemon
COPY . .
EXPOSE 3000
CMD ["node", "-e", "console.log('Hello from cached build v4 - more layer cache testing!'); setTimeout(() => {}, 60000)"]