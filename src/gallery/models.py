from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='photos')
    likes = models.IntegerField(default=0)



