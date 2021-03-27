from django.contrib import admin

# Register your models here.
from .models import NewsData

admin.site.register(NewsData)