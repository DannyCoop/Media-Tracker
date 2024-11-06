from typing import Optional, List
from app.models.user_media import UserMedia

def create_user_media(
        user_id: str, media_id: str
) -> UserMedia:
    user_media: UserMedia = UserMedia(
        user_id=user_id,
        media_id=media_id
    )
    user_media.save()
    return user_media

def get_user_list(user_id) -> List:
    try:
        user_list = UserMedia.collection.filter('user_id', '==', user_id).fetch()
        return user_list
    except Exception:
        return None
    
def delete_user_media(id: str) -> None:
    try:
        UserMedia.collection.delete(id)
    except Exception:
        return None