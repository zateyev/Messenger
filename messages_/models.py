from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    text = models.TextField()
    STATE_NEW = 1
    STATE_DELIVERED = 2
    STATE_READ = 3
    STATE_FAVORITE = 4
    STATE_CHOICES = (
        (STATE_NEW, 'New'),
        (STATE_DELIVERED, 'Delivered'),
        (STATE_READ, 'Read'),
        (STATE_FAVORITE, 'Favorite')
    )
    state = models.IntegerField(choices=STATE_CHOICES)
    sender = models.OneToOneField(User, related_name = 'sender')
    receiver = models.OneToOneField(User, related_name = 'receiver')
    timestamp = models.DateTimeField()

    @classmethod
    def create(cls, text, sender, receiver):
        message = cls(text=text, sender=sender, receiver=receiver, state=1, timestamp= datetime.now(tz=None))
        return message

    def __str__(self):
        return self.text



class FavoriteMessage(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
