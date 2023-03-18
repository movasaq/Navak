import os.path
import uuid

from flask import request, session, abort, jsonify
from werkzeug.utils import secure_filename

import navak_auth.models as UserModel
from navak.extensions import db
from navak_auth.utils import basic_login_required
from navak_config.config import ALLOWED_EXT_IMG, MEDIA_FOLDER
from navak_setting import setting


@setting.route("/change/avatar/", methods=["GET"])
@basic_login_required
def change_avatar_post():
    """
        this view take a post request that contain Image file for chane of set
        profile images for users
    :return: json
    """

    if not (user_db := UserModel.User.query.filter(UserModel.User.id == session.get("account-id")).first()):
        session.clear()
        abort(401)

    if not request.files.get("avatar"):
        return jsonify({"status": "failed", "message": "Missing Some Params"}), 400

    # get file info and obj
    file = request.files.get("avatar")
    fName = file.filename
    fExt = fName.split(".")[-1]

    if fExt not in ALLOWED_EXT_IMG:
        return jsonify({"status": "failed", "message": "File Format is not supported"}), 400

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
            return jsonify({"status": "failed", "message": "Cant Save Image in server"}), 500
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

                return jsonify({"status": "failed", "message": "Cant Save Image in server"}), 500
            else:
                return jsonify({"status": "success", "message": "User Image Profile Changed successfully"}), 200
    else:
        user_old_image = user_db.ProfileImage
        # save new one first then delete old one and commit changes
        try:
            file.save(os.path.join(MEDIA_FOLDER, "profiles", fName))
        except:
            return jsonify({"status": "failed", "message": "Cant Save Image in server"}), 500
        else:
            user_db.ProfileImage = fName
            # delete old one
            if os.path.exists(os.path.join(MEDIA_FOLDER, "profiles", user_old_image)):
                os.remove(os.path.join(MEDIA_FOLDER, "profiles", user_old_image))
            else:
                # delete new images
                if os.path.exists(os.path.join(MEDIA_FOLDER, "profiles", fName)):
                    os.remove(os.path.join(MEDIA_FOLDER, "profiles", fName))

                return jsonify({"status": "failed", "message": "Cant Change User Avatar"}), 500

            # commit changes to db
            db.session.add(user_db)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                return jsonify({"status": "failed", "message": "Cant Change User Avatar"}), 500
            else:
                return jsonify({"status": "success", "message": "User Image Profile Updated successfully"}), 200
