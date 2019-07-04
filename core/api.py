import datetime
import decimal
import json
import uuid

import flask_restful

from flask import request, Response

from core.services.logger import logger


class Api(flask_restful.Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations = {
            'application/json': output_json
        }


class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, uuid.UUID):
            return str(o)
        return super().default(o)


def output_json(data, code, headers=None):
    headers = headers or {}
    output_data = {
        "response_datetime": str(datetime.datetime.utcnow().isoformat()),
        "status": "failure" if code >= 400 else "success",
        "message" if isinstance(data, str) else "data": data
    }
    output_data = json.dumps(output_data, cls=Encoder)
    logger.debug("%d %s => %s", code, request.url, output_data)

    return Response(output_data, code, headers=headers, content_type="application/json")
