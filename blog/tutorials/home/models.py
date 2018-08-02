from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=500)
    post = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author=models.CharField(max_length=300)
    comment=models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
