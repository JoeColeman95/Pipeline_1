FROM python:3.11-slim

RUN pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-grpc

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]