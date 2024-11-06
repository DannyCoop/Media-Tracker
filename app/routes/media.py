from flask import Blueprint, request, make_response
from app.repositories.media_repo import get_seasonal_anime, create_media, get_media, delete_media

blueprint = Blueprint("media", __name__)

@blueprint.route("/get-seasonal-anime", methods=["GET"])
def show_seasonal_anime():
    try:
        media = get_seasonal_anime()
        print(media)
    except Exception as e:
        print(e)
        return make_response(
            {"message": e}
        )
    
    data = {"media": media}
    return make_response(data)

@blueprint.route("/create-media", methods=["POST"])
def create_media_item():
    request_data = request.get_json()

    name = request_data.get("name")
    description = request_data.get("description")

    try:
        create_media(
            name,
            description
        )
    except Exception as e:
        print(e)
        message = {"message": e}
        return make_response(message)
    
    data = {"message": "Media Item created"}
    return make_response(data)

@blueprint.route("/get-media", methods=["GET"])
def get_media_item():
    request_data = request.get_json()

    try:
       media = get_media(request_data.get("id"))
    except Exception as e:
        print(e)
        message = {"message": e}
        return make_response(message)
    
    data = {"data": media}
    return make_response(data)

@blueprint.route("/delete-media", methods=["DELETE"])
def delete_media_item():
    request_data = request.get_json()

    try:
       delete_media(request_data.get("id"))
    except Exception as e:
        print(e)
        message = {"message": e}
        return make_response(message)
    
    data = {"message": "Media deleted"}
    return make_response(data)


# TODO add the route that will let me edit the media

