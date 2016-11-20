from django.contrib.auth.models import User
from django.db import models

from messages_.models import Account


class Registrar(models.Model):
    code = models.SmallIntegerField()

    def generate_code(self):
        # self.code = randint(1, 9999)
        self.code = 1113
        self.send_code()
        return self.code

    @staticmethod
    def register(username, password):
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username)
            user.set_password(password)
            user.save()
            account = Account.create(user)
            account.save()
            return True
        else:
            return False

    def send_code(self):
        print("Your code is: " + str(self.code))
