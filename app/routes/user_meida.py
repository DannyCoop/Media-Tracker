from flask import Blueprint, request, make_response
from app.repositories.user_media_repo import create_user_media, get_user_list, delete_user_media

blueprint = Blueprint("user_media", __name__)



@blueprint.route("/add-to-user-list", methods=["POST"])
def add_to_user_list():
    request_data = request.get_json()
    user_id = request_data.get("user_id")
    media_id = request_data.get("media_id")

    try:
        create_user_media(
            user_id,
            media_id,
        )
    except Exception as e:
        print(e)
        return make_response(
            {"message": e}
        )
    
    data = {"message": "Media added to user list."}
    return make_response(data)

@blueprint.route("/get-user-list", methods=["GET"])
def user_list():
    request_data = request.get_json()
    user_id = request_data.get("user_id")

    try:
        user_list = get_user_list(
            user_id,
        )
    except Exception as e:
        print(e)
        return make_response(
            {"message": e}
        )
    
    data = {"User_list": user_list}
    return make_response(data)

@blueprint.route("/remove-media-from-list", methods=["DELETE"])
def delete_media_from_user_list():
    request_data = request.get_json()
    id = request_data.get("id")

    try:
        delete_user_media(id)
    except Exception as e:
        print(e)
        return make_response(
            {"message": e}
        )
    
    data = {"message": "Media deleted from user list"}
    return make_response(data)
