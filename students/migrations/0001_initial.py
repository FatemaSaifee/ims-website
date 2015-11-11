# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Semester', models.CharField(max_length=15)),
                ('Room_Number', models.CharField(max_length=5)),
                ('Course', models.ForeignKey(to='general.Course')),
                ('Faculty', models.ManyToManyField(to='general.Faculty', verbose_name='faculties', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(unique=True, max_length=100)),
                ('Docfile', models.FileField(upload_to=b'documents/books/')),
                ('pub_date', models.DateTimeField(null=True, verbose_name=b'date published')),
                ('Batch', models.ForeignKey(to='students.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(unique=True, max_length=100)),
                ('URL', models.URLField(unique=True)),
                ('pub_date', models.DateTimeField(null=True, verbose_name=b'date published')),
                ('Batch', models.ForeignKey(to='students.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(unique=True, max_length=100)),
                ('Question_Paper', models.FileField(upload_to=b'documents/books/')),
                ('pub_date', models.DateTimeField(null=True, verbose_name=b'date published')),
                ('Batch', models.ForeignKey(to='students.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Slot', models.CharField(max_length=1, choices=[('1', 'First'), ('2', 'Second')])),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('ID', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=40)),
                ('Batch', models.ForeignKey(to='students.Batch')),
                ('Faculty', models.ForeignKey(to='general.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Time_Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Start_Time', models.TimeField()),
                ('End_Time', models.TimeField()),
                ('Slot', models.ForeignKey(to='students.Slot')),
            ],
        ),
        migrations.CreateModel(
            name='Time_Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Day', models.CharField(max_length=1, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednessday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday')])),
                ('Batch', models.ForeignKey(to='students.Batch')),
                ('Faculty', models.ForeignKey(to='general.Faculty')),
                ('Subject', models.ForeignKey(to='students.Subject')),
                ('Time_Slot', models.ForeignKey(to='students.Time_Slot')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='Slot',
            field=models.ForeignKey(to='students.Slot'),
        ),
    ]
