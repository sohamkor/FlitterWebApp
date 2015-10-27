from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Fleeter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    followerCount = models.IntegerField(default=0)
    followingCount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    fleeter = models.ForeignKey(Fleeter)
    
    contentString = models.CharField(max_length=140)
    dateTimePosted = models.DateTimeField('date published')

    def __str__(self):
        return self.contentString

class Follower(models.Model):
    userWhoIsBeingFollowed = models.ForeignKey(Fleeter, related_name='originalUserWhoIsBeingFollowed')
    
    theUserWhoIsFollowing = models.ForeignKey(Fleeter, related_name='theUserWhoIsFollowing')

    def __str__(self):
        return self.theUserWhoIsFollowing.user.username + " -> " + self.userWhoIsBeingFollowed.user.username
