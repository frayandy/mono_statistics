import os
import logging


class Config:
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEBUG = False
    HOST = '127.0.0.1'
    LOG_LEVEL = logging.INFO
    TOKEN = os.environ.get('TOKEN', None)


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", "dev").strip().lower()
    if env == "prod":
        return ProdConfig

    return DevConfig
