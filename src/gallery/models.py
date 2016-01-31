from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        title = self.image.name
        super(Gallery, self).save(*args, **kwargs)









