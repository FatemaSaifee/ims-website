# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='link',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='question_paper',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published'),
        ),
    ]
