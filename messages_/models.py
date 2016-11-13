from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
    state = models.IntegerField(choices=STATE_CHOICES, default=STATE_NEW)
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    timestamp = models.DateTimeField(default=timezone.now)

    @classmethod
    def create(cls, text, sender, receiver):
        message = cls(text=text, sender=sender, receiver=receiver)
        return message

    def __str__(self):
        return self.text


class Account(models.Model):
    user = models.ForeignKey(User)
    inbox = models.ManyToManyField(Message, related_name='inbox')
    sent = models.ManyToManyField(Message, related_name='sent')
    starred = models.ManyToManyField(Message, related_name='starred')

    @classmethod
    def create(cls, user):
        account = cls(user=user)
        return account


class FavoriteMessage(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)

    @classmethod
    def create(cls, message, user):
        favorite_message = cls(message=message, user=user)
        return favorite_message
