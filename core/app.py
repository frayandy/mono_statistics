from flask import Flask

from core.api import Api
from core.config import runtime_config
from core.resources.smoke import SmokeResource

app = Flask(__name__)
app.config.from_object(runtime_config())

api = Api(app, prefix='/mono-statistics')
api.add_resource(SmokeResource, '/smoke')
