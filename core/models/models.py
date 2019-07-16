import base64

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID as PUUID
from sqlalchemy.ext.declarative import declarative_base

from core.utils.utils import generate_uuid

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(PUUID(as_uuid=True), primary_key=True, default=generate_uuid)
    name = Column(String)
    surname = Column(String)
    token = Column(String)

    def set_token(self, password):
        self.token = base64.b64encode(password)

    def decode_token(self):
        return base64.b16decode(self.token)
