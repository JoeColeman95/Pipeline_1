FROM node:18-alpine
WORKDIR /app
# Added this comment to trigger cache invalidation - v5
# Testing :latest tag layer caching functionality
RUN echo "Installing dependencies and utilities..." && npm install -g nodemon eslint
COPY . .
EXPOSE 3000
CMD ["node", "-e", "console.log('Hello from cached build v5 - final layer cache test!'); setTimeout(() => {}, 60000)"]
#new commit
#again
#another change
#final change
# This is a final comment to ensure the Dockerfile is complete and ready for use.
# This line is to ensure the Dockerfile is complete and ready for use.
# This is a final comment to ensure the Dockerfile is complete and ready for use.
# fds