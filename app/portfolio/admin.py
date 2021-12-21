from django.contrib import admin
from .models import Category, Album, Image

# Register your models here.
admin.site.register(Category)
admin.site.register(Album)
admin.site.register(Image)
