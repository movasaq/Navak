from flask import Blueprint


auth = Blueprint("auth", __name__, static_folder="public_static", template_folder="template")

import navak_auth.views