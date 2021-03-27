import datetime

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
from django.forms import Textarea, TextInput


class User(models.Model):
    username = models.CharField(blank=False, max_length=20)
    password = models.TextField()

    def get_absolute_url(self):
        return '.'


class NewsData(models.Model):
    url = models.TextField()
    title = models.TextField()
    author = models.CharField(null=True, default='NA', max_length=100)
    description = models.TextField(null=True)
    content = models.TextField(null=True)
    pub_date = models.CharField(null=True, max_length=30)
    urlImage = models.TextField(null=True)
    category = models.CharField(default='general', max_length=20)
    date = models.DateField(default=datetime.date.today)

    def get_absolute_url(self):
        return reverse('display_article', kwargs={'category': self.category, 'url': str(self.url).split("/")[-1]})
