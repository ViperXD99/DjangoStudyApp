from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room (models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) #One topic can have several Rooms
    # null = True in above line because when the topic set Null at on delete the database should allow that
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    #participants =
    updated = models.DateTimeField(auto_now= True) # The datetime will updated everytime when save
    created = models.DateTimeField(auto_now_add=True) # The Date Time will updated at the 1st save only

    #Creating the string representation for the class
    def __str__(self):
        return self.name 
    

class Message (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now= True) # The datetime will updated everytime when save
    created = models.DateTimeField(auto_now_add=True) # The Date Time will updated at the 1st save only

    def __str__(self):
        return self.body[0:50]