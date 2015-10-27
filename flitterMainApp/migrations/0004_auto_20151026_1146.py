# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flitterMainApp', '0003_remove_fleeter_postcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='fleeter',
            field=models.ForeignKey(related_name='originalUserWhoIsBeingFollowed', to='flitterMainApp.Fleeter'),
        ),
    ]
