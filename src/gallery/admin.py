from django.contrib import admin

# Register your models here.
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'likes')
    list_display = ('title', 'likes')

admin.site.register(Gallery, GalleryAdmin)