from django.db import models
# from students.models import  Batch
from django.contrib.auth.models import User
from django.forms import ModelForm
# from students.models import Time_Slot
from django.core.urlresolvers import reverse


# Create your models here.
#Table structure for table `Faculty_Info`

class Faculty(models.Model):
	User = models.OneToOneField(User, on_delete=models.CASCADE)#This is the user_id from User_master table.
	Name=models.CharField(max_length=50)
	#Discipline =models.CharField(max_length=200)
	Designation=models.CharField(max_length=200)
	Responsibility=models.CharField(max_length=200)
	DOJ=models.DateField() 		#Date of Joining
	Qualification=models.CharField(max_length=200)
	Area_Of_Interest=models.CharField(max_length=200)
	Previous_Job=models.CharField(max_length=200)
	Web_Link=models.CharField(max_length=40,default=None)
	Blog_Link=models.CharField(max_length=40,default=None)
	Alternate_Email=models.CharField(max_length=40,default=None)
	Linkedin_Link=models.CharField(max_length=40,default=None)
	Facebook_Link=models.CharField(max_length=40,default=None)
	Googleplus_Link=models.CharField(max_length=40,default=None)
	Twitter_Link=models.CharField(max_length=40,default=None)
	Picture=models.URLField(max_length=100,default=None)
	Resume =models.URLField(max_length=40,default=None)#Link to resume
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse('faculty:profile')

class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        exclude = ['User']

class Faculty_Time_Table(models.Model):
    DAY_CHOICES = (
        (u'1', u'Monday'),
        (u'2', u'Tuesday'),
        (u'3', u'Wednessday'),
        (u'4', u'Thursday'),
        (u'5', u'Friday'),
        (u'6', u'Saturday'),
    )
    Faculty = models.ForeignKey(Faculty)
    Day = models.CharField(max_length=1, choices=DAY_CHOICES)
    Time_Slot = models.ForeignKey('students.Time_Slot')
    Subject = models.CharField(max_length=20)
    Subject_Id = models.CharField(max_length=10)
    Batch = models.ForeignKey('students.Batch')

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.Batch)
