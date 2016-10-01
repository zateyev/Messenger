from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField()
    STATE_NEW = 1
    STATE_DELIVERED = 2
    STATE_READ = 3
    STATE_FAVORITE = 4
    STATE_CHOICES = (
        (STATE_NEW, 'New'),
        (STATE_DELIVERED, 'New'),
        (STATE_READ, 'New'),
        (STATE_FAVORITE, 'New')
    )
    state = models.IntegerField(choices=STATE_CHOICES)
    sender = models.OneToOneField(User)
    # receiver = models.OneToOneField(User)
    timeStamp = models.DateTimeField()

    def __str__(self):
        return self.text


class FavoriteMessage(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
