from uuid import uuid4
from django.db import models


class User(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=132)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
