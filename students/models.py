from django.db import models
# from apps.faculty.models import Faculty
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from general.models import Course
from django.forms import ModelForm
from django.core.urlresolvers import reverse
# from registration.models import RegistrationProfile
import registration

# Create your models here.
class Slot(models.Model):
    SLOT_CHOICES = (
        (u'1', u'First'),
        (u'2', u'Second'),
        )
    Slot = models.CharField(max_length=1, choices=SLOT_CHOICES)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.Slot

class Batch(models.Model):
    Course=models.ForeignKey(Course)
    Semester=models.CharField(max_length=15)
    Faculty =  models.ManyToManyField('general.Faculty', verbose_name=_('faculties'), blank=True
    )
    Room_Number = models.CharField(max_length=5)
    Slot =models.ForeignKey(Slot)

    def __unicode__(self):  # Python 3: def __str__(self)
        return str(self.Course.name + ' ' + self.Semester)
        

class Subject(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Batch = models.ForeignKey('students.Batch') 
    Name = models.CharField(max_length=40)
    Faculty = models.ForeignKey('general.Faculty') 

    def __unicode__(self):  # Python 3: def __str__(self)
        return self.Name

class Time_Slot(models.Model):
    
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
    Slot = models.ForeignKey(Slot)

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.Start_Time) + ' - ' + str(self.End_Time)

class Time_Table(models.Model):
    DAY_CHOICES = (
        (u'1', u'Monday'),
        (u'2', u'Tuesday'),
        (u'3', u'Wednessday'),
        (u'4', u'Thursday'),
        (u'5', u'Friday'),
        (u'6', u'Saturday'),
    )
    Day = models.CharField(max_length=1, choices=DAY_CHOICES)
    Time_Slot = models.ForeignKey(Time_Slot)
    Subject = models.ForeignKey(Subject)
    Faculty = models.ForeignKey('general.Faculty')
    Batch = models.ForeignKey(Batch)

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.Subject)

   
# class Notification(models.Model):
#     Title = models.CharField(max_length=100)
#     Link = models.URLField()
#     pub_date = models.DateTimeField('date published')
    
#     def __unicode__(self):  # Python 3: def __str__(self):
#         return self.Title

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Book(models.Model):
    Batch = models.ForeignKey(Batch)
    Title = models.CharField(max_length=100, unique=True)
    Docfile = models.FileField(upload_to='documents/books/')
    pub_date = models.DateTimeField('date published', null=True)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.Title


class Question_Paper(models.Model):
    Batch = models.ForeignKey(Batch)
    Title = models.CharField(max_length=100, unique=True)
    Question_Paper = models.FileField(upload_to='documents/books/')
    pub_date = models.DateTimeField('date published', null=True)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.Title

class Link(models.Model):
    Batch = models.ForeignKey(Batch)
    Title = models.CharField(max_length=100, unique=True)
    URL = models.URLField(unique=True)
    pub_date = models.DateTimeField('date published', null=True)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.Title