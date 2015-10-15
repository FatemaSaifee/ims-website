from django.db import models
# from students.models import  Batch
from django.contrib.auth.models import User
# from students.models import Time_Slot
from django.core.urlresolvers import reverse
# from registration.models import RegistrationProfile

# Create your models here.
#Table structure for table `Faculty_Info`


class Faculty_Time_Table(models.Model):
    DAY_CHOICES = (
        (u'1', u'Monday'),
        (u'2', u'Tuesday'),
        (u'3', u'Wednessday'),
        (u'4', u'Thursday'),
        (u'5', u'Friday'),
        (u'6', u'Saturday'),
    )
    Faculty = models.ForeignKey('general.Faculty')
    Day = models.CharField(max_length=1, choices=DAY_CHOICES)
    Time_Slot = models.ForeignKey('students.Time_Slot')
    Subject = models.CharField(max_length=20)
    Subject_Id = models.CharField(max_length=10)
    Batch = models.ForeignKey('students.Batch')

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.Batch)
