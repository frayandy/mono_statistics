import json
import functools
import decimal
import datetime
import uuid


class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, datetime.date):
            return o.isoformat()
        if isinstance(o, uuid.UUID):
            return str(o)
        return super().default(o)


custom_json_dumps = functools.partial(json.dumps, cls=Encoder)
