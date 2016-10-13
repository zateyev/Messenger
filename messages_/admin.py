from django.contrib import admin

# Register your models here.
from messages_.models import Message
admin.site.register([Message])


