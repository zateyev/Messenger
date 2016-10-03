from django import forms
from django.db import models
from django.contrib.auth.models import User
from random import randint


class Registrar(models.Model):
    code = models.SmallIntegerField()

    def generate_code(self):
        self.code = randint(1, 9999)
        self.send_code()
        return self.code

    @staticmethod
    def register(username, password):
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username)
            user.password = password
            user.save()
            return True
        else:
            return False

    def send_code(self):
        print("Your code is: " + str(self.code))
