from fireo.models import Model
from fireo.fields import TextField, IDField, DateTime
from datetime import datetime, timezone
from typing import Any

class User(Model):
    id = IDField()

    first_name = TextField()
    last_name = TextField()
    display_name = TextField()
    email = TextField()

    created_at = DateTime(default=datetime.utcnow())
    last_updated_at = DateTime()

    def save(self) -> Any:
        self.last_updated_at = datetime.now(timezone.utc)
        return super().save()
