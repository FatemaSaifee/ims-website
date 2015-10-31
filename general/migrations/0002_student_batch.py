# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Batch',
            field=models.ForeignKey(to='students.Batch', null=True),
        ),
    ]
