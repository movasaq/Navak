from flask import Flask

from navak.extensions import db_migrate, SessionServer, db, csrf
from navak_config import config as config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Development)

    # register extensions
    SessionServer.init_app(app)
    db.init_app(app)
    db_migrate.init_app(app=app, db=db)
    csrf.init_app(app)

    from navak_auth import auth
    app.register_blueprint(auth, url_prefix="/auth")

    from navak_gard import gard
    app.register_blueprint(gard, url_prefix="/gard")

    return app


app = create_app()

import navak.views
