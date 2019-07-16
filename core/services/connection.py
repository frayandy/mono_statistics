from threading import Lock

from flask import current_app
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from sqlalchemy import create_engine

from core.models.models import Base
from core.services.logger import logger
from core.utils.utils import custom_json_dumps

engine_lock = Lock()
engine = None


def get_db_uri(user=None, password=None, host=None, port=None, db_name=None):
    return current_app.config['DB_URI'].format(
        user=user or current_app.config['DB_USER'],
        password=password or current_app.config['DB_PASSWORD'],
        host=host or current_app.config['DB_HOST'],
        port=port or current_app.config['DB_PORT'],
        db_name=db_name or current_app.config['DB_NAME'],
    )


def get_engine(uri):
    global engine

    with engine_lock:

        if not engine:
            engine = create_engine(uri, poolclass=QueuePool, json_serializer=custom_json_dumps)

        try:
            engine.execute('select 1')
        except SQLAlchemyError as e:
            logger.error(str(e))
            engine = create_engine(uri, poolclass=QueuePool, json_serializer=custom_json_dumps)

    return engine


def get_connection():
    return get_engine(get_db_uri()).connect()


def create_database(db_name: str = None):
    default_engine = create_engine(
        get_db_uri(db_name=current_app.config['DEFAULT_DB']), poolclass=NullPool, isolation_level='AUTOCOMMIT'
    )
    db_name = db_name or current_app.config['DB_NAME']

    if not default_engine.execute(f"SELECT 1 from pg_database WHERE datname='{db_name}'").fetchone():
        default_engine.execute(f"CREATE DATABASE {db_name}")

        db_engine = get_engine(get_db_uri(db_name=db_name))
        Base.metadata.create_all(db_engine)
        db_engine.dispose()

    default_engine.dispose()


def drop_database(db_name: str = None):
    default_engine = create_engine(
        get_db_uri(db_name=current_app.config['DEFAULT_DB']), poolclass=NullPool, isolation_level='AUTOCOMMIT'
    )
    db_name = db_name or current_app.config['DB_NAME']
    if default_engine.execute(f"SELECT 1 from pg_database WHERE datname='{db_name}'").fetchone():
        default_engine.execute(f"DROP DATABASE {db_name}")
    default_engine.dispose()
