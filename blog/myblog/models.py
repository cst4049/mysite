# coding:utf-8
from django.db import models

class Article(models.Model):
    URL=models.URLField()
    title=models.CharField(max_length=50)
    title_zh=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    content=models.TextField()
    tags=models.CharField(max_length=30)
    views=models.IntegerField()
    created=models.DateTimeField()
    updated=models.DateTimeField()
    def __unicode__(self):
        return self.title
    
class GuestBook(models.Model):
    user=models.CharField(max_length=50)
    content=models.TextField()
    created=models.DateTimeField()
    def __unicode__(self):
        return self.user
    

