from django.db import models

class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username  # Return the username, not self.User