from navak_config.utils import load_education, load_roles


def get_all_education():
    """
        this function return all education degrees in tuple format
        for wtforms
    :return: tuple
    """
    education = load_education()
    data = []
    for each in education:
        data.append((each["name"], each["name"],))

    return data


def get_all_work_position():
    """
        this function return all workPositions in tuple format
        for wtforms
    :return: tuple
    """
    education = load_roles()
    data = []
    for each in education:
        data.append((each["role-fa"], each["role-fa"],))

    return data
