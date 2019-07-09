from core.resources.base import BaseResource


class SmokeResource(BaseResource):

    def get(self):
        return 'ok', 200
