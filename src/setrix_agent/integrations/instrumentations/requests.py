from ..base import safe_import


def instrument():
    module = safe_import(
        "opentelemetry.instrumentation.requests",
        "pip install setrix-agent[requests-trace]",
    )

    RequestsInstrumentor = module.RequestsInstrumentor
    RequestsInstrumentor().instrument()
