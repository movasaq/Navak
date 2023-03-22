from khayyam import JalaliDatetime


def validate_date(dt: str):
    """
        this function take a string date like=> "2023/10/1"
        and make sure that input is date
    :return: JalaliDatetime.date if valid date otherWise False
    """

    if len(dt_arry := dt.split("/")) != 3:
        return False

    try:
        dt_obj = JalaliDatetime(year=dt_arry[-3], month=dt_arry[-2], day=dt_arry[-1])
        return dt_obj.date()
    except ValueError:
        return False


def validate_phone(dt: str):
    """
        this view take an phone number ins tring format and validate it
    :return: phone:int if valid phonenumber otherWise False
    """

    if len(dt) != 11:
        return False

    if not dt.isdigit():
        return False

    return dt
