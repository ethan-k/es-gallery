from django.db import models

# Create your models here.

class Gallery(models.Model):
    likes = models.IntegerField(default=0)


