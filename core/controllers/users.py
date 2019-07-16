from uuid import UUID

from flask import g

from core.controllers import BaseController
from core.models.models import Users


class UsersController(BaseController):

    def get_user_by_id(self, user_id: UUID) -> dict:
        user = self.get_user(user_id)
        data = dict(user)
        del data['token']
        return data

    def get_users(self):
        return g.session.query(Users).all()
