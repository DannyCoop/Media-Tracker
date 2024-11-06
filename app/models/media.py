from fireo.models import Model
from fireo.fields import TextField, IDField, DateTime
from datetime import datetime, timezone
from typing import Any


class Media(Model):
    id = IDField()
    name = TextField()
    description = TextField()
    # TODO This will most likely turn in to datetime just not sure how yet
    next_update = TextField()

    created_at = DateTime(default=datetime.utcnow())
    last_updated_at = DateTime()

    def save(self):
        self.last_updated_at = datetime.now(timezone.utc)
        return super().save()
