from django.db import models
#from django.conf import settings
#from django.utils.text import slugify
#from django.db.models.signals import pre_save
#from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='article/', default='default.jpg', blank=True, null=True)
    date = models.DateTimeField()
    content = models.TextField()
    draft = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class Hero(models.Model):
    image = models.ImageField(upload_to='hero/', default='default.jpg')
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    caption = models.CharField(max_length=200)
    sub_headings = models.CharField(max_length=100)


    def __str__(self):
        return self.caption
