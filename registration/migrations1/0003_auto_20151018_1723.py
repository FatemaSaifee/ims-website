# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_registrationprofile_activated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='RegistrationProfile',
        ),
    ]
