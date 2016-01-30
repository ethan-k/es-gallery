from django.contrib import admin

# Register your models here.
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    fields = ('image', 'likes')

admin.site.register(Gallery, GalleryAdmin)