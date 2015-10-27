# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flitterMainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='fleeter',
            field=models.ForeignKey(related_name='originalUserWhoIsBeingFollwed', to='flitterMainApp.Fleeter'),
        ),
        migrations.AlterField(
            model_name='follower',
            name='usernameOfFollower',
            field=models.ForeignKey(related_name='theUserWhoIsFollowing', to='flitterMainApp.Fleeter'),
        ),
        migrations.AlterField(
            model_name='following',
            name='fleeter',
            field=models.ForeignKey(related_name='originalUserWhoIsFollowing', to='flitterMainApp.Fleeter'),
        ),
        migrations.AlterField(
            model_name='following',
            name='usernameOfFollowing',
            field=models.ForeignKey(related_name='theUserWhoIsBeingFollowed', to='flitterMainApp.Fleeter'),
        ),
    ]
