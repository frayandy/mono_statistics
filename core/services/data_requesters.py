import requests

from http import HTTPStatus
from typing import List

from flask_restful import abort

from core.models.models import Users


class BaseDataRequester:
    _base_url = 'https://api.monobank.ua'
    _specific_url = None

    def make_url(self, **kwargs):
        return '{base}/{specific}'.format(base=self._base_url, specific=self._specific_url.format(**kwargs))

    @staticmethod
    def make_headers(user_token: str) -> dict:
        return {'Content-type': 'application/json', 'X-Token': user_token}


class StatisticsDataRequester(BaseDataRequester):
    _specific_url = 'personal/statement/{account}/{start_time}/{end_time}'

    def get_statistics_per_time(self, user: Users, start_time: int, end_time: int) -> List[dict]:
        response = requests.get(self.make_url(account=user.account, start_time=str(start_time)), end_time=str(end_time))
        if response.status_code != HTTPStatus.OK:
            abort(response.status_code, message=response.json()['errorDescription'])

        return response.json()
