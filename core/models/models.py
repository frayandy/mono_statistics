from sqlalchemy import MetaData, Table, Column, String
from sqlalchemy.dialects.postgresql import UUID as PUUID

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('user_id', PUUID, primary_key=True),
    Column('name', String(255)),
    Column('surname', String(255)),
    Column('token', String(255))
)
