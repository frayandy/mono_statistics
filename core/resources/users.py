from uuid import UUID

from flask import request

from core.forms import UserSchema
from core.resources.base import BaseResource
from core.controllers.users import UsersController


class UserResource(BaseResource):

    def get(self, user_id: UUID):
        controller = UsersController()
        return controller.get_user_by_id(user_id)


class UsersResource(BaseResource):

    def post(self):
        user_data, errors = UserSchema().load(request.json)
        if errors:
            return errors, 422

        controller = UsersController()
        return controller.add_user(user_data)

    def get(self):
        controller = UsersController()
        return controller.get_users()
