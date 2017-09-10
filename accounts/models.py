from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from django.db import models


# Create your models here.


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    hometown = models.CharField(max_length=140, blank=True, null=True)
    facebook_id = models.CharField(max_length=40, blank=True, null=True)
    facebook_picture_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.username)
