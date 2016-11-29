from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Message(models.Model):
    text = models.TextField()
    STATE_NEW = 1
    STATE_READ = 2
    STATE_FAVORITE = 3
    STATE_CHOICES = (
        (STATE_NEW, 'New'),
        (STATE_READ, 'Read'),
        (STATE_FAVORITE, 'Favorite')
    )
    state = models.IntegerField(choices=STATE_CHOICES, default=STATE_NEW)
    sender = models.ForeignKey(User, related_name='outbox')
    receiver = models.ForeignKey(User, related_name='inbox')
    is_visible = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
