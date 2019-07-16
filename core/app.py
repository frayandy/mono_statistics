from flask import Flask, g
from sqlalchemy.orm import sessionmaker

from core.api import Api
from core.config import runtime_config
from core.resources.smoke import SmokeResource
from core.resources.users import UserResource, UsersResource
from core.services.connection import get_connection

app = Flask(__name__)
app.config.from_object(runtime_config())


@app.before_request
def open_session():
    g.conn = get_connection()
    session = sessionmaker()
    session.configure(bind=g.conn)
    g.session = session()


@app.teardown_request
def close_session(e):
    if 'session' in g:
        if e is None:
            g.session.commit()
        else:
            g.session.rollback()

        g.session.close()
        g.session = None


api = Api(app, prefix='/mono-statistics')
api.add_resource(SmokeResource, '/smoke')
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<uuid:user_id>')
