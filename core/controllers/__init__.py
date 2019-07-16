from uuid import UUID
from http import HTTPStatus

from flask import g
from flask_restful import abort

from core.models.models import Users


class BaseController:

    @staticmethod
    def get_user(user_id: UUID) -> Users:
        user = g.session.query(Users).filter_by(user_id == user_id).first()
        if not user:
            abort(HTTPStatus.NOT_FOUND, message='User not found')

        return user
