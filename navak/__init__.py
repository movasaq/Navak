from flask import Flask
from navak.extensions import  db_migrate, SessionServer, db



def create_app():
    app = Flask(__name__)

    # register extensions
    SessionServer.init_app(app)
    db.init_app(app)
    db_migrate(app=app, db=db)

    return app


app = create_app()

import navak.views