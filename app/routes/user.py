from flask import Blueprint, request, make_response
from app.repositories.user_repo import create_user, update_user, delete_user

blueprint = Blueprint("user", __name__)

@blueprint.route("/create-user", methods=["POST"])
def make_user():
    request_data = request.get_json()

    first_name = request_data.get("first_name")
    last_name = request_data.get("last_name")
    display_name = request_data.get("display_name")
    email=request_data.get("email")
    print("Executing")

    try:
        create_user(
            first_name,
            last_name,
            display_name,
            email
        )
    except Exception as e:
        print(e)
        return make_response(
            {"message": e}
        )
    
    data = {"message": "User successfully created"}
    return make_response(data)

@blueprint.route("/update-user", methods=["POST"])
def update_user_info():
    request_data = request.get_json()

    id = request_data.get("id")
    print("This is the user_id", id)
    first_name = request_data.get("first_name")
    last_name = request_data.get("last_name")
    display_name = request_data.get("display_name")
    email=request_data.get("email")

    update_data = {}
    if first_name is not None:
        update_data["first_name"] = first_name
    else:
        update_data["first_name"] = None
    if last_name is not None:
        update_data["last_name"] = last_name
    else:
        update_data["last_name"] = last_name
    if display_name is not None:
        update_data["display_name"] = display_name
    else:
        update_data["display_name"] = display_name
    if email is not None:
        update_data["email"] = email
    else:
        update_data["email"] = email

    try:
        update_user(id, **update_data)
    except Exception as e:
        print(e)
        return make_response(
            {"message": e}
        )
    
    data = {"message": "Update successfully"}
    return make_response(data)

@blueprint.route("/remove-user", methods=["DELETE"])
def remove_user():
    request_data = request.get_json()
    id = request_data.get("id")

    try:
        delete_user(id)
    except Exception as e:
        print(e)
        return make_response(
            {"message": e}
        )
    
    data = {"message": "User deleted"}
    return make_response(data)


