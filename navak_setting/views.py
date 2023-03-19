import os.path
import uuid

from flask import request, session, abort, send_from_directory, redirect, flash
from werkzeug.utils import secure_filename

import navak_auth.models as UserModel
from navak.extensions import db
from navak_auth.utils import basic_login_required
from navak_config.config import ALLOWED_EXT_IMG, MEDIA_FOLDER
from navak_setting import setting
from navak_setting.utils import UserTag


@setting.route("/image/", methods=["GET"])
@basic_login_required
def serve_user_image():
    """
    this view serve user image profile
    :return: Media/Image
    """
    if not (user_db := UserModel.User.query.filter(UserModel.User.id == session.get("account-id")).first()):
        session.clear()
        abort(401)

    if os.path.exists(os.path.join(MEDIA_FOLDER, "profiles", user_db.ProfileImage)):
        return send_from_directory(os.path.join(MEDIA_FOLDER, "profiles"), user_db.ProfileImage)
    else:
        return "File Not Found!", 404


@setting.route("/change/avatar/", methods=["POST"])
@basic_login_required
def change_avatar_post():
    """
        this view take a post request that contain Image file for chane of set
        profile images for users
    """

    if not (user_db := UserModel.User.query.filter(UserModel.User.id == session.get("account-id")).first()):
        session.clear()
        abort(401)

    if not request.files.get("profile-img"):
        flash("برخی مقادیر مقدار دهی نشده است", "danger")
        return redirect(request.referrer)

    # get file info and obj
    file = request.files.get("profile-img")
    fName = file.filename
    fExt = fName.split(".")[-1]

    if fExt not in ALLOWED_EXT_IMG:
        flash("نوع فایل وارد شده پشتیبانی نمی شود", "danger")
        return redirect(request.referrer)

    # secure file name => bd04fbbb-714a-450e-91cb-cd5166d4891fhello.jpg
    fName = str(uuid.uuid4()) + secure_filename(fName)[-50:]

    # check if user avatar is default just replace it and save new image
    # otherwise delete old one and replace new one
    if user_db.ProfileImage == "default.png":
        user_db.ProfileImage = fName
        try:
            file.save(os.path.join(MEDIA_FOLDER, "profiles", fName))
        except:
            # check if file is save wrong delete it
            if os.path.exists(os.path.join(MEDIA_FOLDER, "profiles", fName)):
                os.remove(os.path.join(MEDIA_FOLDER, "profiles", fName))
            flash("خطایی رخ داد بعدا دوباره امتحان کنید", "danger")
            return redirect(request.referrer)
        else:
            # if file is ok
            # change user profile image and commit changes
            db.session.add(user_db)
            try:
                db.session.commit()
            except:
                # if something goes wrong rollback changes
                # delete user new image profile
                db.session.rollback()
                # delete image
                if os.path.exists(os.path.join(MEDIA_FOLDER, "profiles", fName)):
                    os.remove(os.path.join(MEDIA_FOLDER, "profiles", fName))

                flash("خطایی رخ داد بعدا دوباره امتحان کنید", "danger")
                return redirect(request.referrer)
            else:
                flash("عملیات با موفقیت انجام گردید", "success")
                return redirect(request.referrer)
    else:
        user_old_image = user_db.ProfileImage
        # save new one first then delete old one and commit changes
        try:
            file.save(os.path.join(MEDIA_FOLDER, "profiles", fName))
        except:
            flash("خطایی رخ داد بعدا دوباره امتحان کنید", "danger")
            return redirect(request.referrer)
        else:
            user_db.ProfileImage = fName
            # delete old one
            if os.path.exists(os.path.join(MEDIA_FOLDER, "profiles", user_old_image)):
                os.remove(os.path.join(MEDIA_FOLDER, "profiles", user_old_image))
            else:
                # delete new images
                if os.path.exists(os.path.join(MEDIA_FOLDER, "profiles", fName)):
                    os.remove(os.path.join(MEDIA_FOLDER, "profiles", fName))

                flash("خطایی رخ داد بعدا دوباره امتحان کنید", "danger")
                return redirect(request.referrer)

            # commit changes to db
            db.session.add(user_db)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash("خطایی رخ داد بعدا دوباره امتحان کنید", "danger")
                return redirect(request.referrer)
            else:
                flash("عملیات با موفقیت انجام شد", "success")
                return redirect(request.referrer)


@setting.route("/change/tag/", methods=["POST"])
@basic_login_required
def change_user_tag():
    """
        this view take a post request for change user tag
    :return:
    """
    if not (user_db := UserModel.User.query.filter(UserModel.User.id == session.get("account-id")).first()):
        session.clear()
        abort(401)

    if not (tag := request.form.get("user-tag")):
        flash("برخی موارد به نظر مقدار دهی نشده است", "danger")
        return redirect(request.referrer)

    TagUser = UserTag(tag)
    if not TagUser.is_Verify():
        flash("شناسه کاربری وارد شده با پیش نیاز های مورد نیاز همخوانی ندارد", "danger")
        return redirect(request.referrer)

    user_db.Usertag = request.form.get("user-tag")
    db.session.add(user_db)

    try:
        db.session.commit()
    except:
        db.session.rollback()
    else:
        flash("عملیات با موفقیت انجام شد", "success")
        return redirect(request.referrer)
