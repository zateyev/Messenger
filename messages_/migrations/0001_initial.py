# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-29 02:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('state', models.IntegerField(choices=[(1, 'New'), (2, 'Read'), (3, 'Favorite')], default=1)),
                ('is_visible', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inbox', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outbox', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
