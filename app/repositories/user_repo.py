from typing import Optional
from app.models.user import User

def create_user(
        first_name: str, last_name: str, display_name: str, email: str 
) -> str:
    user: User = User(
        first_name=first_name,
        last_name=last_name,
        display_name=display_name,
        email=email,
    )
    print("Prep Save")
    user.save()
    print("End Save")
    return id

def get_user(id: str) -> User:
    try:
        user = User.collection.get(id)
        return user
    except Exception:
        return None
    

def update_user(
        id: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        display_name: Optional[str]= None,
        email: Optional[str] = None,
) -> None:
    user: User = get_user(id)
    # TODO Add checks to make sure people can't change info to the same info
    print("This is the user", user.display_name)

    updates = {
        "first_name": first_name,
        "last_name": last_name,
        "display_name": display_name,
        "email": email,
    }

    for key, value in updates.items():
        if value is not None:
            setattr(user, key, value)

    user.update()
    return None

def delete_user(id: str) -> None:
    try:
        User.collection.delete(id)
    except Exception:
        return None
