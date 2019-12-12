from datetime import datetime
from uuid import UUID

from flask import g

from core.controllers import BaseController
from core.models.models import Users


class UsersController(BaseController):

    def get_user_by_id(self, user_id: UUID) -> dict:
        user = dict(self.get_user(user_id))
        del user['token']
        return user

    def get_users(self):
        return g.session.query(Users).all()

    def add_user(self, user_data: dict) -> dict:
        user_data['create_time'] = datetime.now()
        user = Users(**user_data)
        g.session.add(user)
        return user
