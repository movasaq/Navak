import json

import navak_config.config as config


def load_roles():
    """
        this function return all roles from json conf file

    :return: dict(Roles)
    """
    json_path = (config.BASE_DIR / "navak_config" / "roles.json")
    fp = open(file=json_path)
    j = json.loads(fp.read())
    fp.close()
    return j["navak_roles"]
