import os
import time

print("="*50)
print("Container Environment Variables:")
print(f"TRACEPARENT: {os.getenv('TRACEPARENT', 'NOT SET')}")
print(f"TRACESTATE: {os.getenv('TRACESTATE', 'NOT SET')}")
print(f"OTEL_EXPORTER_OTLP_ENDPOINT: {os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'NOT SET')}")
print(f"OTEL_EXPORTER_OTLP_HEADERS: {os.getenv('OTEL_EXPORTER_OTLP_HEADERS', 'NOT SET')}")
print(f"OTEL_EXPORTER_OTLP_PROTOCOL: {os.getenv('OTEL_EXPORTER_OTLP_PROTOCOL', 'NOT SET')}")
print("="*50)

try:
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

    print("Creating spans...")
    with tracer.start_as_current_span("container.main"):
        print("In container.main span")
        time.sleep(0.5)

        with tracer.start_as_current_span("container.task"):
            print("In container.task span")
            time.sleep(0.5)

    print("Flushing spans...")
    provider.force_flush()
    print("Container finished successfully!")

except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
