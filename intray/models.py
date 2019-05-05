import uuid
from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_text

    item_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    item_text = models.TextField()
    is_archived = models.BooleanField(default=False)
