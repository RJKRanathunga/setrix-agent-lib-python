from ..base import safe_import


def instrument():
    module = safe_import(
        "opentelemetry.instrumentation.httpx",
        "pip install setrix-agent[httpx]",
    )

    HTTPXClientInstrumentor = module.HTTPXClientInstrumentor
    HTTPXClientInstrumentor().instrument()
