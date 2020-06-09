from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Image(models.Model):
    location = models.CharField(max_length=100)
    gps = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100)

    @classmethod
    def create(cls, name,gps,location):
        image = cls(location=location,gps=gps,name=name)
        return image


class Challenge(models.Model):
    picture = models.ForeignKey(Image,null=True,on_delete=models.CASCADE)
    initiator= models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    description= models.TextField()
    title = models.CharField(max_length=50,default="Mystery")
    coordinates = models.CharField(max_length=50)
    rating = models.FloatField()

    @classmethod
    def create(cls, picture,initiator,description,title,coordinates,rating):
        image = cls (picture = picture,initiator = initiator,description = description ,title = title,coordinates = coordinates,rating = rating)
        return image

class Cache(models.Model):
    origin = models.ForeignKey(Challenge,on_delete=models.SET_NULL,null=True,related_name="origin")
    isStep=models.BooleanField()
    next_challenge= models.ForeignKey(Challenge,on_delete=models.SET_NULL,null=True,related_name="next")
    isHint = models.BooleanField()

class Solved(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    challenge= models.ForeignKey(Challenge,on_delete=models.CASCADE)

class marked(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    challenge= models.ForeignKey(Challenge,on_delete=models.CASCADE)





