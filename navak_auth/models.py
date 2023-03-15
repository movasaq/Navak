import uuid
import khayyam
from navak.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer, DateTime, Boolean



class Role(db.Model):
    """
        base Model For Users Role
    """
    __tablename__ = "navak_roles"
    id = Column(Integer(), primary_key=True)
    RoleName = Column(String(64))
    RoleDescription = Column(String(256))
    Users = db.relationship("User", backref="Role", lazy="True")


class User(db.Model):
    __tablename__ = "navak_users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(102), nullable=False)

    FullName = Column(String(102), nullable=True)
    CreatedTime = Column(DateTime(), default=khayyam.JalaliDatetime.now)
    Active = Column(Boolean(), default=False)
    ProfileImage = Column(String(256), default="default.png", nullable=False)
    UserSignature = Column(String(256), nullable=True)

    # user id in chat
    Usertag = Column(String(128), nullable=True, default=None, unique=True)
    PublicKey = Column(String(36), nullable=False, unique=True)

    UserRole = Column(Integer(), db.ForeignKey("navak_roles.id"), nullable=False)


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_public_key(self):
        """
            This Method Set Unique PublicKey For Users Object
        """
        while True:
            key = str(uuid.uuid4())
            key_db = User.query.filter(User.PublicKey == key).first()
            if key_db:
                continue
            else:
                self.PublicKey = key
                return None

