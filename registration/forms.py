"""
Forms and validation code for user registration.

Note that all of these forms assume Django's bundle default ``User``
model; since it's not possible for a form to anticipate in advance the
needs of custom user models, you will need to write your own forms if
you're using a custom model.

"""
from __future__ import unicode_literals

# to remove ValueError: Cannot assign "...": "MyRelatedModel" instance isn't saved in the database.
import contextlib

@contextlib.contextmanager
def allow_unsaved(model, field):
    model_field = model._meta.get_field(field)
    saved = model_field.allow_unsaved_instance_assignment
    model_field.allow_unsaved_instance_assignment = True
    yield
    model_field.allow_unsaved_instance_assignment = saved


from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from general.models import Student, Faculty
from .users import UserModel, UsernameField

# for multiple forms (registrationprofile, faculty, student) in class based form view
from multiform import MultiModelForm
import pdb


User = UserModel()

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['user','activation_key','activated','verified']#,'Batch','Father_Name','Mother_Name','DOB','Roll_Number','Enrollment_Number']
        # fields = '__all__'
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        # }

class RegistrationForm(MultiModelForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    # required_css_class = 'required'
    # email = forms.EmailField(label=_("E-mail"))
    # # group = forms.CharField(label = ("Category"))
    # class Meta:
    #     model = Student
    #     fields = '__all__'#(UsernameField(), "email")#,"group")
  
    base_forms = [
            ('user', UserCreateForm),
            ('student', StudentForm),
            
        ]

    def dispatch_init_instance(self, name, instance):
        if name == 'student':
            return instance
        return super(RegistrationForm, self).dispatch_init_instance(name, instance)

    def save(self, commit=True):
        """Save both forms and attach the user to the person."""
        instances = super(RegistrationForm, self).save(commit=False)
        with allow_unsaved(Student, 'user'):
            instances['student'].user = instances['user']
        # instances['student'].user = instances['user']
        if commit:
            user = instances['user']
            user.save()
            profile = instances['student']
            profile.user = user
            profile.save()
            # for instance in instances.values():
            #     # instance.user_id = 1
            #     instance.save()
        return instances


    # def save(self, **kwargs):
    #     users = User.objects.filter(pk__in=kwargs.get('users', None))
    #     roles = Role.objects.filter(pk__in=kwargs.get('roles', None))
    #     project = kwargs.get('project', None)

    #     for user in users:
    #         member, created = Member.objects.get_or_create(project=project, user=user)
    #         if created:
    #             for role in roles:
    #                 member.roles.add(role)


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        exclude = ['user','activation_key','activated','verified']


class FacultyRegistrationForm(MultiModelForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    
    base_forms = [
            ('user', UserCreateForm),
            ('faculty', FacultyForm), 
        ]

    def dispatch_init_instance(self, name, instance):
        if name == 'Faculty':
            return instance
        return super(FacultyRegistrationForm, self).dispatch_init_instance(name, instance)

    def save(self, commit=True):
        """Save both forms and attach the user to the person."""
        instances = super(FacultyRegistrationForm, self).save(commit=False)
        with allow_unsaved(Student, 'user'):
            instances['faculty'].user = instances['user']
        
        if commit:
            user = instances['user']
            user.save()
            profile = instances['faculty']
            profile.user = user
            profile.save()
            
        return instances       

class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """
    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_('I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.

    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.

    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.

    """
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.

        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']
