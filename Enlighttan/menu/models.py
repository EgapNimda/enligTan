from django.db import models
from django.contrib.auth.models import User

class chant(models.Model):
    name = models.CharField(max_length=50)
    chanting = models.CharField(max_length=1000)

