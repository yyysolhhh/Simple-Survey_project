from configs import settings

TORTOISE_APP_MODELS = [
    "app.models.article",
    "app.models.comment",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": settings.DB_HOST,
                "port": settings.DB_PORT,
                "user": settings.DB_USER,
                "password": settings.DB_PASSWORD,
                "database": settings.DB_DB,
                "connect_timeout": 5,
            },
        },
    },
    "apps": {
        "models": {
            "models": TORTOISE_APP_MODELS,
        },
    },
    # "routers": ["app.configs.database_config.Router"],
    "timezone": "Asia/Seoul",
}
