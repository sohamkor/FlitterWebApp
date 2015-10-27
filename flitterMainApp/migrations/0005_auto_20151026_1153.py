# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flitterMainApp', '0004_auto_20151026_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='usernameOfFollower',
            new_name='theUserWhoIsFollowing',
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='fleeter',
            new_name='userWhoIsBeingFollowed',
        ),
        migrations.RenameField(
            model_name='following',
            old_name='usernameOfFollowing',
            new_name='theUserWhoIsBeingFollowed',
        ),
        migrations.RenameField(
            model_name='following',
            old_name='fleeter',
            new_name='userWhoIsFollowing',
        ),
    ]
