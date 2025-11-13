import os
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

resource = Resource.create({"service.name": "test-container-app"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

print(f"TRACEPARENT: {os.getenv('TRACEPARENT', 'NOT SET')}")
print(f"OTEL_EXPORTER_OTLP_ENDPOINT: {os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'NOT SET')}")

with tracer.start_as_current_span("container.main"):
    print("Creating span in container...")
    time.sleep(0.5)
    
    with tracer.start_as_current_span("container.task"):
        print("Doing some work...")
        time.sleep(0.5)

print("Container finished!")
provider.force_flush()
