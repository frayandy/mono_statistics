from uuid import UUID

from core.controllers import BaseController


class UsersController(BaseController):

    def get_user_by_id(self, user_id: UUID) -> dict:
        user = self.get_user(user_id)
        data = dict(user)
        del data['token']
        return data
