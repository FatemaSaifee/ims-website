# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jqchat', '0001_initial'),
        ('students', '0001_initial'),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='Room',
            field=models.ForeignKey(to='jqchat.Room', unique=True),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='User',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='Batch',
            field=models.ForeignKey(to='students.Batch', null=True),
        ),
    ]
