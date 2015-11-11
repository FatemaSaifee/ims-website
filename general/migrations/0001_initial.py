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
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Heading', models.CharField(default=b'Address', max_length=50, choices=[(b'Address', b'Address'), (b'Contact_No', b'Contact No.'), (b'Email_Address', b'Email Address'), (b'Hours', b'Working Hours'), (b'Facebook', b'Facebook'), (b'Linkedin', b'Linkedin'), (b'Google+', b'Google+'), (b'Twitter', b'Twitter')])),
                ('Description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('number_of_semester', models.PositiveSmallIntegerField(null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('objective', models.TextField(max_length=2000, null=True)),
                ('highlight', models.TextField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=100)),
                ('Docfile', models.FileField(upload_to=b'documents/news/')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=100)),
                ('Link', models.URLField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('activated', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'registration profile',
                'verbose_name_plural': 'registration profiles',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('registrationprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='general.RegistrationProfile')),
                ('Name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=200)),
                ('Responsibility', models.CharField(max_length=200)),
                ('DOJ', models.DateField()),
                ('Qualification', models.CharField(max_length=200)),
                ('Area_Of_Interest', models.CharField(max_length=200)),
                ('Previous_Job', models.CharField(max_length=200)),
                ('Web_Link', models.CharField(default=None, max_length=40)),
                ('Blog_Link', models.CharField(default=None, max_length=40)),
                ('Alternate_Email', models.CharField(default=None, max_length=40)),
                ('Linkedin_Link', models.CharField(default=None, max_length=40)),
                ('Facebook_Link', models.CharField(default=None, max_length=40)),
                ('Googleplus_Link', models.CharField(default=None, max_length=40)),
                ('Twitter_Link', models.CharField(default=None, max_length=40)),
                ('Picture', models.URLField(default=None, max_length=100)),
                ('Resume', models.URLField(default=None, max_length=40)),
            ],
            bases=('general.registrationprofile',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('registrationprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='general.RegistrationProfile')),
                ('Father_Name', models.CharField(max_length=200)),
                ('Mother_Name', models.CharField(max_length=200)),
                ('DOB', models.DateField(max_length=200)),
                ('Local_Address', models.CharField(default=None, max_length=200, blank=True)),
                ('Permanent_Address', models.CharField(default=None, max_length=200)),
                ('Mobile_Number', models.CharField(max_length=15, blank=True)),
                ('Telephone_Number', models.CharField(default=None, max_length=200, blank=True)),
                ('Roll_Number', models.CharField(default=None, max_length=200)),
                ('Enrollment_Number', models.CharField(default=None, max_length=200)),
                ('Picture', models.URLField(default=None, blank=True)),
            ],
            bases=('general.registrationprofile',),
        ),
        migrations.AddField(
            model_name='registrationprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ForeignKey(to='general.Program'),
        ),
    ]
