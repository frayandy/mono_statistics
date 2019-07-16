from flask_script import Manager

from core.app import app
from core.services.connection import create_database, drop_database

manager = Manager(app)


@manager.command
@manager.option('-p', '--port', help='Server port')
@manager.option('-h', '--host', help='Server host')
def runserver(host, port):
    app.run(host, port)


@manager.command
def init_db():
    with app.app_context():
        create_database()


@manager.command
def drop_db():
    with app.app_context():
        drop_database()


if __name__ == "__main__":
    manager.run()
