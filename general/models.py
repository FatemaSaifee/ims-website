from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from jqchat.models import Room
from django.utils.encoding import python_2_unicode_compatible
from registration.users import UserModel, UserModelString
from registration.models import RegistrationManager
from django.forms import ModelForm
from ims_site import settings
	
try:
    from django.utils.timezone import now as datetime_now
except ImportError:
    datetime_now = datetime.datetime.now

# Create your models here.

# class Profile(models.Model):
#     #add any common fields here (first_name, last_name and email come from User)

#     #perhaps add is_student or is_teacher properites here
#     @property
#     def is_student(self):
#         try:
#             self.student
#             return True
#         except Student.DoesNotExist:
#             return False

#     @property
#     def is_faculty(self):
#         try:
#             self.faculty
#             return True
#         except Faculty.DoesNotExist:
#             return False
            
@python_2_unicode_compatible
class RegistrationProfile(models.Model):
    """
    A simple profile which stores an activation key for use during
    user account registration.

    Generally, you will not want to interact directly with instances
    of this model; the provided manager includes methods
    for creating and activating new accounts, as well as for cleaning
    out accounts which have never been activated.

    While it is possible to use this model as the value of the
    ``AUTH_PROFILE_MODULE`` setting, it's not recommended that you do
    so. This model's sole purpose is to store data temporarily during
    account registration and activation.

    """
    # user = models.OneToOneField(UserModelString(), verbose_name=_('user'), null = True)
    user = models.OneToOneField(User)
    activation_key = models.CharField(_('activation key'), max_length=40)
    activated = models.BooleanField(default=False)

    objects = RegistrationManager()

    class Meta:
        verbose_name = _('registration profile')
        verbose_name_plural = _('registration profiles')

    def __str__(self):
        return "Registration information for %s" % self.user


    @property
    def is_student(self):
        try:
            self.student
            return True
        except Student.DoesNotExist:
            return False

    @property
    def is_faculty(self):
        try:
            self.faculty
            return True
        except Faculty.DoesNotExist:
            return False

    def activation_key_expired(self):
        """
        Determine whether this ``RegistrationProfile``'s activation
        key has expired, returning a boolean -- ``True`` if the key
        has expired.

        Key expiration is determined by a two-step process:

        1. If the user has already activated, ``self.activated`` will
           be ``True``. Re-activating is not permitted, and so this
           method returns ``True`` in this case.

        2. Otherwise, the date the user signed up is incremented by
           the number of days specified in the setting
           ``ACCOUNT_ACTIVATION_DAYS`` (which should be the number of
           days after signup during which a user is allowed to
           activate their account); if the result is less than or
           equal to the current date, the key has expired and this
           method returns ``True``.

        """
        expiration_date = datetime.timedelta(
            days=settings.ACCOUNT_ACTIVATION_DAYS)
        return (self.activated or
                (self.user.date_joined + expiration_date <= datetime_now()))
    activation_key_expired.boolean = True

    def send_activation_email(self, site, request=None):
        """
        Send an activation email to the user associated with this
        ``RegistrationProfile``.

        The activation email will make use of two templates:

        ``registration/activation_email_subject.txt``
            This template will be used for the subject line of the
            email. Because it is used as the subject line of an email,
            this template's output **must** be only a single line of
            text; output longer than one line will be forcibly joined
            into only a single line.

        ``registration/activation_email.txt``
            This template will be used for the text body of the email.

        ``registration/activation_email.html``
            This template will be used for the html body of the email.

        These templates will each receive the following context
        variables:

        ``user``
            The new user account

        ``activation_key``
            The activation key for the new account.

        ``expiration_days``
            The number of days remaining during which the account may
            be activated.

        ``site``
            An object representing the site on which the user
            registered; depending on whether ``django.contrib.sites``
            is installed, this may be an instance of either
            ``django.contrib.sites.models.Site`` (if the sites
            application is installed) or
            ``django.contrib.sites.requests.RequestSite`` (if
            not). Consult the documentation for the Django sites
            framework for details regarding these objects' interfaces.

        ``request``
            Optional Django's ``HttpRequest`` object from view.
            If supplied will be passed to the template for better
            flexibility via ``RequestContext``.
        """
        ctx_dict = {}
        if request is not None:
            ctx_dict = RequestContext(request, ctx_dict)
        # update ctx_dict after RequestContext is created
        # because template context processors
        # can overwrite some of the values like user
        # if django.contrib.auth.context_processors.auth is used
        ctx_dict.update({
            'user': self.user,
            'activation_key': self.activation_key,
            'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
            'site': site,
        })
        subject = (getattr(settings, 'REGISTRATION_EMAIL_SUBJECT_PREFIX', '') +
                   render_to_string(
                       'registration/activation_email_subject.txt', ctx_dict))
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        from_email = getattr(settings, 'REGISTRATION_DEFAULT_FROM_EMAIL',
                             settings.DEFAULT_FROM_EMAIL)
        message_txt = render_to_string('registration/activation_email.txt',
                                       ctx_dict)

        email_message = EmailMultiAlternatives(subject, message_txt,
                                               from_email, [self.user.email])

        if getattr(settings, 'REGISTRATION_EMAIL_HTML', True):
            try:
                message_html = render_to_string(
                    'registration/activation_email.html', ctx_dict)
            except TemplateDoesNotExist:
                pass
            else:
                email_message.attach_alternative(message_html, 'text/html')

        email_message.send()

class Faculty(RegistrationProfile):
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



class Program(models.Model):
	name=models.CharField(max_length=30)
	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

class Student(RegistrationProfile):
    Batch = models.ForeignKey('students.Batch')
    Father_Name =models.CharField(max_length=200)
    Mother_Name =models.CharField(max_length=200)
    DOB= models.DateField(max_length=200)
    Local_Address =models.CharField(max_length=200,default=None,blank=True)
    Permanent_Address =models.CharField(max_length=200,default = None)
    Mobile_Number =models.CharField(max_length=15,blank=True)
    Telephone_Number =models.CharField(max_length=200,default=None,blank=True)
    Roll_Number =models.CharField(max_length=200,default = None)
    Enrollment_Number =models.CharField(max_length=200,default=None)
    Picture=models.URLField(default=None,blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('students:profile')




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

