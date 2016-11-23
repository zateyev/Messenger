# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-23 14:12
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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('state', models.IntegerField(choices=[(1, 'New'), (2, 'Delivered'), (3, 'Read'), (4, 'Favorite')], default=1)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='inbox',
            field=models.ManyToManyField(related_name='inbox', to='messages_.Message'),
        ),
        migrations.AddField(
            model_name='account',
            name='sent',
            field=models.ManyToManyField(related_name='sent', to='messages_.Message'),
        ),
        migrations.AddField(
            model_name='account',
            name='starred',
            field=models.ManyToManyField(related_name='starred', to='messages_.Message'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
