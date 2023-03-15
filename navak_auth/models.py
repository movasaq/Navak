import uuid
import datetime as dt
from navak.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer, DateTime, Boolean, JSON


class User(db.Model):
    __tablename__ = "navak_users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(102), nullable=False)

    public_username = Column(String(256), nullable=True)
    created_at = Column(DateTime(), default=dt.datetime.now)
    active = Column(Boolean(), default=False)

    image = Column(String(256), default="default.png", nullable=False)
    signature = Column(String(256), nullable=True)

    # user id in chat
    user_tag = Column(String(128), nullable=True, default=None, unique=True)

    # user public chat key
    public_key = Column(String(36), nullable=False, unique=True)

    # this relate user to a group
    # user_group = Column(Integer(), db.ForeignKey("navak_groups.id"), nullable=False)

    # this defind user access users can have multiply roles
    user_role = Column(JSON())

    # employee_id = db.relationship("Employee", backref="user", lazy=True)
    # ProjectStatus = db.relationship("ProjectStatus", backref="user", lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_public_key(self):
        """
            generate a public key for user
            first query to db for checking db for key
        """
        while True:
            key = str(uuid.uuid4())
            key_db = User.query.filter(User.public_key == key).first()
            if key_db:
                continue
            else:
                self.public_key = key
                return None

