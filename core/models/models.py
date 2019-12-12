import base64
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, UniqueConstraint, DateTime
from sqlalchemy.dialects.postgresql import UUID as PUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(PUUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False, default=datetime.now)
    __table_args__ = (UniqueConstraint("name", "last_name"),)

    def set_token(self, password):
        self.token = base64.b64encode(password)

    def decode_token(self):
        return base64.b16decode(self.token)


class Statistic(Base):
    __tablename__ = 'spending'
    statistic_id = Column(PUUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
