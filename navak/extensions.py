from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


SessionServer = Session()
db = SQLAlchemy()
db_migrate = Migrate()