from flask import Flask

from core.api import Api
from core.resources.smoke import SmokeResource

app = Flask(__name__)
api = Api(app, prefix='/mono-statistics')

api.add_resource(SmokeResource, '/smoke')
