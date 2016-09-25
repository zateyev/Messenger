from django.db import models
from django.contrib.auth.models import User


class MessageState(enumerate):
    NEW = 1
    DELIVERED = 2
    READ = 3
    FAVORITE = 4


class Message(models.Model):
    text = models.TextField()
    messageState = models.ForeignKey(MessageState)
    sender = models.OneToOneField(User)
    receiver = models.OneToOneField(User)
    timeStamp = models.DateTimeField()

    def render(self):
        return self.text


class FavoriteMessages(models.Model):
    messages = models.ForeignKey(Message)
