from django.conf import settings
from django.db import models
from django.utils import timezone

class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.IntegerField(blank=True)
