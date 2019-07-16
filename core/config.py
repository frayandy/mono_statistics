import os
import logging

from core.constants import APP_ENV_DEV, APP_ENV_PROD


class Config:
    DB_USER = os.environ.get('DB_USER', 'camunda')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'camunda')
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEBUG = False
    HOST = '127.0.0.1'
    LOG_LEVEL = logging.INFO
    TOKEN = os.environ.get('TOKEN', None)
    DB_NAME = os.environ.get('DB_NAME')
    DB_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig

    return DevConfig
