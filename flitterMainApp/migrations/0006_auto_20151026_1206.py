# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flitterMainApp', '0005_auto_20151026_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='theUserWhoIsBeingFollowed',
        ),
        migrations.RemoveField(
            model_name='following',
            name='userWhoIsFollowing',
        ),
        migrations.DeleteModel(
            name='Following',
        ),
    ]
