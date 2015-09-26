from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from jqchat.models import Room

# Create your models here.
class Program(models.Model):
	name=models.CharField(max_length=30)
	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

class Course(models.Model):

	DISCIPLINE_CHOICES = (
        ('TECHNICAL', 'Technical'),
        ('MANAGEMENT', 'Management'),
    )
    
	
	name = models.CharField(max_length=200)
	program = models.ForeignKey('Program')
	number_of_semester = models.PositiveSmallIntegerField(null=True)
	# Discipline = models.CharField(max_length=12, choices=DISCIPLINE_CHOICES, default='MANAGEMENT')
	description = models.TextField(max_length=2000,null=True)
	objective = models.TextField(max_length=2000,null=True)
	highlight = models.TextField(max_length=2000,null=True)
	
	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

class News(models.Model):
	Title = models.CharField(max_length=100)
	Docfile = models.FileField(upload_to='documents/news/')
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Title

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Notification(models.Model):
	Title = models.CharField(max_length=100)
	Link = models.URLField()
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Title

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Contact(models.Model):
	HEADING_CHOICES = (
        ('Address','Address'),
        ('Contact_No','Contact No.'),
        ('Email_Address','Email Address'),
        ('Hours','Working Hours'),
        ('Facebook','Facebook'),
        ('Linkedin','Linkedin'),
        ('Google+','Google+'),
        ('Twitter','Twitter'),
    )

	Heading = models.CharField(max_length=50,choices=HEADING_CHOICES, default='Address')
	Description = models.TextField(max_length=100)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Heading



class ChatRoom(models.Model):
	Room = models.ForeignKey(Room, unique = True)
	User = models.ForeignKey(User)

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Room
