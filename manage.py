from core.app import app
from flask_script import Manager


manager = Manager(app)


@manager.option('-p', '--port', help='Server port')
@manager.option('-h', '--host', help='Server host')
def runserver(host, port):
    app.run(host, port)


if __name__ == "__main__":
    manager.run()
