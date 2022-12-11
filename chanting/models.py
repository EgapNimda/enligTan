from django.db import models

class praying(models.Model): # praying table
    title = models.CharField(max_length=25) # ชื่อบทสวด
    content = models.CharField(max_length=1000) # เนื้อบทสวด
