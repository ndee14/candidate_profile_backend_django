import uuid

from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(null=True, default=True)
    status = models.CharField(max_length=55, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__}(uuid={self.uuid})"
