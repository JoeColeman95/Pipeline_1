FROM alpine:latest

RUN apk add --no-cache curl

WORKDIR /app

COPY . .

CMD ["echo", "Hello from test app!"]