# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postCount', models.IntegerField(default=0)),
                ('followerCount', models.IntegerField(default=0)),
                ('followingCount', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernameOfFollower', models.CharField(max_length=90)),
                ('fleeter', models.ForeignKey(to='flitterMainApp.Fleeter')),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernameOfFollowing', models.CharField(max_length=90)),
                ('fleeter', models.ForeignKey(to='flitterMainApp.Fleeter')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentString', models.CharField(max_length=140)),
                ('dateTimePosted', models.DateTimeField(verbose_name='date published')),
                ('fleeter', models.ForeignKey(to='flitterMainApp.Fleeter')),
            ],
        ),
    ]
