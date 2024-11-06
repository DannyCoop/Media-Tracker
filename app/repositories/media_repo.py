from typing import Optional
from app.models.media import Media
from datetime import datetime
from app.utils.media_util import get_season
import requests

# Adding a new piece of media to the firestore
def create_media(
    name: str, description: str
) -> str:
    print("Start")
    media: Media = Media(
        name = name,
        description = description
    )
    print("Media created")


    media.save()
    print("meadia save")
    return id

# This refers to getting a piece of media from firestore
def get_media(id) -> Media:
    try:
       media = Media.collection.get(id)
       return media

    except Exception:
        return None
    
# updating media info on firestore
def update_media(
        id: str,
        description: Optional[str] = None,
        next_update: Optional[str] = None,
) -> None:
    media = get_media(id)

    updates = {
        "description": description,
        "next_update": next_update,
    }

    for key, value in updates:
        if value is not None:
            setattr(media, key, value)
        
    media.update()
    return None

# Deleting media from firestore
def delete_media(id: str) -> None:
    try:
        Media.collection.delete(id)
    except Exception:
        return None
    
def get_seasonal_anime():
    try:
        r = requests.get(f'https://api.jikan.moe/v4/seasons/now')
        return r.json()
    except Exception as e:
        return e