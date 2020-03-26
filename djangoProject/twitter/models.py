import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
    # User Object
    username = models.CharField(max_length=50, default="")
    firstName = models.CharField(max_length=50, default="")
    lastName = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=25, default="")
    followers = models.ManyToManyField('self')
    following = models.ManyToManyField('self')

class Post(models.Model):
    # Post Object
    userName = models.CharField(max_length=45, default="no username")
    bodyText = models.CharField(max_length=200, default='no body text')
    dateCreated = models.DateTimeField("datePosted",default='')
    likes = models.IntegerField(default = 0)
    userId = models.CharField(max_length=15, default='@')
    likedBy = models.ManyToManyField(User)
