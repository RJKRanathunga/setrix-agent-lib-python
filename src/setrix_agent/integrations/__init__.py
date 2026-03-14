FRAMEWORKS = {
    "flask": "setrix_agent.integrations.frameworks.flask:instrument",
    "fastapi": "setrix_agent.integrations.frameworks.fastapi:instrument",
    "django": "setrix_agent.integrations.frameworks.django:instrument",
}

INSTRUMENTATIONS = {
    "requests": "setrix_agent.integrations.instrumentations.requests:instrument",
    "httpx": "setrix_agent.integrations.instrumentations.httpx:instrument",
    "psycopg2": "setrix_agent.integrations.instrumentations.psycopg2:instrument",
    "sqlalchemy": "setrix_agent.integrations.instrumentations.sqlalchemy:instrument",
}
