from fireo.models import Model
from fireo.fields import TextField, IDField, DateTime
from datetime import datetime, timezone
from typing import Any

class UserMedia(Model):
    id = IDField
    user_id = TextField()
    media_id = TextField()

    created_at = DateTime(default=datetime.utcnow())
    last_updated_at = DateTime()

    def save(self) -> Any:
        self.last_updated_at = datetime.now(timezone.utc)
        return super().save()
