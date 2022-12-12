from django.db import models

class praying(models.Model): # praying table
    title = models.CharField(max_length=25) # ชื่อบทสวด
    slug = models.CharField(max_length=25)
    content = models.CharField(max_length=1000) # เนื้อบทสวด

class prayingset(models.Model):
    title = models.CharField(max_length=25) # ชื่อบทสวด
    slug = models.CharField(max_length=25)
    set = models.ManyToManyField(praying)

