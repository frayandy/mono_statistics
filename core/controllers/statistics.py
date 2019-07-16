from datetime import datetime, timedelta
from typing import Tuple
from uuid import UUID

from core.controllers import BaseController
from core.services.data_requesters import StatisticsDataRequester


class StatisticsController(BaseController):
    _data_getter = StatisticsDataRequester()

    def get_last_month_statistics(self, user_id: UUID):
        user = self.get_user(user_id)
        start_time, end_time = self._get_data_range_from_now(days=30)
        return self._data_getter.get_statistics_per_time(user, start_time, end_time)

    @staticmethod
    def _get_data_range_from_now(days: int) -> Tuple[int, int]:
        date_now = datetime.utcnow()
        date_end = date_now - timedelta(days=days)
        return int(date_now.timestamp()), int(date_end.timestamp())
