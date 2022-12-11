from django.db import models
from chanting.models import praying


class myuser(models.Model): # user table 
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    fav = models.ManyToManyField(praying)


