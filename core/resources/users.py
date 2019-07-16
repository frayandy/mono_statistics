from uuid import UUID

from core.resources.base import BaseResource
from core.controllers.users import UsersController


class UserResource(BaseResource):

    def get(self, user_id: UUID):
        controller = UsersController()
        return controller.get_user_by_id(user_id)


class UsersResource(BaseResource):

    def get(self):
        controller = UsersController()
        return controller.get_users()
