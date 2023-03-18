import datetime
from pathlib import Path

# allowed file extensions
ALLOWED_EXT_IMG = ["jpg", "png"]

# C:\Users\Public\samane-navak  -----> root_path
BASE_DIR = Path(__file__).parent.parent

# login Paths
LOGIN_PATHS_MATTERIAL = [
    ["employee", "admin", "gard", "engineer", "office"],
    ["کارمند", "ادمین", "حراست", "مهندس", "اداری"]
]
LOGIN_PATHS = [each for each in zip(LOGIN_PATHS_MATTERIAL[0], LOGIN_PATHS_MATTERIAL[1])]

# Static files Path
LOGIN_PUBLIC_STATIC = BASE_DIR / "navak" / "logins_public"
MEDIA_FOLDER = BASE_DIR / "navak_media"

# DB INFO
USERNAME_DB = "navak"
PASSWORD_DB = "123654"
HOST_DB = "localhost"
PORT_DB = 3307
NAME_DB = "navak"



class config:
    SECRET_KEY = "Hello world!"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session configuration
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=16)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_NAME = '_session_cookie_'

    # WTF_CSRF_ENABLED = False


class Development(config):
    DEBUG = True
    FLASK_DEBUG = True


class Production(config):
    DEBUG = False
    FLASK_DEBUG = False
