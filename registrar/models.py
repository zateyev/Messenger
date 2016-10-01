from django import forms
from django.db import models
from django.contrib.auth.models import User
from random import randint


class Registrar(models.Model):
    code = models.SmallIntegerField()

    def generate_code(self):
        self.code = randint(1, 9999)
        print("Your code is: " + str(self.code))
        return self.code

    @staticmethod
    def register(username, password):
        user = User.objects.create_user(username)
        user.password = password
        user.save()

    def send_code(self):
        pass
