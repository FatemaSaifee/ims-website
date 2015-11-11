from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone
from django.contrib import auth

from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import pdb

import django_filters


class Account_HomeView(ListView):
    model = Program
    template_name = 'general/account-index.html'

    def get_context_data(self, **kwargs):
        ctx = super(Account_HomeView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['notification_list']= Notification.objects.order_by('-pub_date')[:5]
        
        user = self.request.user

        if user is not None:
            try:
                Student.objects.get(user=user)
                is_student = True
            except Student.DoesNotExist:
                is_student = False
            try:
                Faculty.objects.get(user=user)
                is_faculty = True
            except Faculty.DoesNotExist:
                is_faculty = False

            if is_student:
                ctx['accountbase'] = 'students/base.html'
            if is_faculty:
                ctx['accountbase'] = 'faculty/base.html'
        return ctx

# class AccountProgramView(ListView):
#     model = Program
#     template_name = 'general/account-program.html'

#     def get_queryset(self):
#         return Program.objects.all()


# @login_required
class AccountProgramDetailView(SingleObjectMixin, ListView):
    
    template_name = "general/account-programdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Program.objects.all())
        return super(AccountProgramDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AccountProgramDetailView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        
        user = self.request.user

        if user is not None:
            try:
                Student.objects.get(user=user)
                is_student = True
            except Student.DoesNotExist:
                is_student = False
            try:
                Faculty.objects.get(user=user)
                is_faculty = True
            except Faculty.DoesNotExist:
                is_faculty = False

            if is_student:
                ctx['accountbase'] = 'students/base.html'
            if is_faculty:
                ctx['accountbase'] = 'faculty/base.html'
        return ctx

    def get_queryset(self):
        return self.object.course_set.all()

# @login_required
class AccountNewsView(ListView):
    model = News
    template_name = 'general/account-news.html'

    def get_context_data(self, **kwargs):
        ctx = super(AccountNewsView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        
        user = self.request.user

        if user is not None:
            try:
                Student.objects.get(user=user)
                is_student = True
            except Student.DoesNotExist:
                is_student = False
            try:
                Faculty.objects.get(user=user)
                is_faculty = True
            except Faculty.DoesNotExist:
                is_faculty = False

            if is_student:
                ctx['accountbase'] = 'students/base.html'
            if is_faculty:
                ctx['accountbase'] = 'faculty/base.html'

        return ctx


    
# @login_required
class AccountNotificationView(ListView):
    model = Notification
    template_name = 'general/account-notification.html'

    
    def get_context_data(self, **kwargs):
        ctx = super(AccountNotificationView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        
        user = self.request.user

        if user is not None:
            try:
                Student.objects.get(user=user)
                is_student = True
            except Student.DoesNotExist:
                is_student = False
            try:
                Faculty.objects.get(user=user)
                is_faculty = True
            except Faculty.DoesNotExist:
                is_faculty = False

            if is_student:
                ctx['accountbase'] = 'students/base.html'
            if is_faculty:
                ctx['accountbase'] = 'faculty/base.html'

        return ctx

# @login_required
class AccountContactView(ListView):
    model = Contact
    template_name = 'general/account-contact.html' 

    def get_context_data(self, **kwargs):
        ctx = super(AccountContactView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        
        user = self.request.user

        if user is not None:
            try:
                Student.objects.get(user=user)
                is_student = True
            except Student.DoesNotExist:
                is_student = False
            try:
                Faculty.objects.get(user=user)
                is_faculty = True
            except Faculty.DoesNotExist:
                is_faculty = False

            if is_student:
                ctx['accountbase'] = 'students/base.html'
            if is_faculty:
                ctx['accountbase'] = 'faculty/base.html'

        return ctx 

# @login_required
class AccountFacultyInfoView(ListView):
    context_object_name= 'item_list'
    template_name = 'general/account-facultyinfo.html'   

    def get_queryset(self):
        return Faculty.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(AccountFacultyInfoView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        
        user = self.request.user

        if user is not None:
            try:
                Student.objects.get(user=user)
                is_student = True
            except Student.DoesNotExist:
                is_student = False
            try:
                Faculty.objects.get(user=user)
                is_faculty = True
            except Faculty.DoesNotExist:
                is_faculty = False

            if is_student:
                ctx['accountbase'] = 'students/base.html'
            if is_faculty:
                ctx['accountbase'] = 'faculty/base.html'

        return ctx  


# # @login_required
# def AccountFacultyView(request):
#     context= {}
#     context['program_list'] = Program.objects.all()
#     context['time_slot_list'] = Time_Slot.objects.all()
#     context['notification_list'] = Notification.objects.all().order_by('-pub_date')[:5]
#     context['user']=request.user
#     # time table lists
    
#     days = ['monday','tuesday','wednessday','thursday','friday','saturday']
#     day_number = 0
#     for day in days:
#         context[day] = []
#         day_number += 1
#         time_table = request.user.faculty.faculty_time_table_set.filter(Day=day_number)
#         for time in Time_Slot.objects.all():
#             for item in time_table:
#                 if item.Time_Slot == time:
#                     context[day].append(item)
#                     break
#             else:
#                 context[day].append('-')
#     return render_to_response('faculty/bulletin.html', context)

    #context['profile']=request.user.profile #Profile.objects.get('User'=request__user)#request.user.profile
    
class HomeView(ListView):
    model = Program
    template_name = 'general/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['notification_list']= Notification.objects.order_by('-pub_date')[:5]

        
        return ctx

# class ProgramView(ListView):
#     model = Program
#     template_name = 'general/program.html'

#     def get_queryset(self):
#         return Program.objects.all()



class ProgramDetailView(SingleObjectMixin, ListView):
    
    template_name = "general/programdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Program.objects.all())
        return super(ProgramDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(ProgramDetailView, self).get_context_data(**kwargs)
        # pdb.set_trace()
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx
    def get_queryset(self):
        return self.object.course_set.all()

class FacultyDetailView(generic.DetailView):
    
    template_name = "general/facultydetail.html"
    model = Faculty

    def get_context_data(self, **kwargs):
        ctx = super(FacultyDetailView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        

        return ctx





# class NotificationView(ListView):
#     model = Notification
#     template_name = 'general/notification.html'

# class NotificationFilter(django_filters.FilterSet):
#     pub_date = django_filters.DateFilter(lookup_type='lt')
    
#     class Meta:
#         model = Notification
#         fields =  fields = {'pub_date': ['lt', 'gt'],
#                          }
#         order_by = ['pub_date']

    
#     def get_context_data(self, **kwargs):
#         ctx = super(NotificationView, self).get_context_data(**kwargs)
#         ctx['program_list'] = Program.objects.all()
#         ctx['course_list'] = Course.objects.all()

#         return ctx

# def NotificationView(request):
#     f = NotificationFilter(request.GET, queryset=Notification.objects.order_by('pub_date'))#.all())
#     return render_to_response('general/notification.html', {'filter': f})

def NotificationView(request):

    start = request.GET.get('start','')
    end = request.GET.get('end','')

    response = render_to_response('general/notification.html',
                                {'notification_list': Notification.objects.filter(pub_date__range=[start,end])
                                })
                                  # context=RequestContext(self.request))
        # response['Content-Type'] = 'text/plain; charset=utf-8'
        # response['Cache-Control'] = 'no-cache'
    
    
    # pdb.set_trace()
    return response

# If you want to access the filtered objects in your views, for example if you want to paginate them, you can do that. They are in f.qs
def NewsView(request):

    start = request.GET.get('start','')
    end = request.GET.get('end','')

    response = render_to_response('general/news.html',
                                {'news_list': News.objects.filter(pub_date__range=[start,end])
                                })
                                 
    return response

def NoticeView(request):

    start = request.GET.get('start','')
    end = request.GET.get('end','')

    response = render_to_response('general/notice.html',
                                {'notification_list': Notification.objects.filter(pub_date__range=[start,end]),
                                'news_list': News.objects.filter(pub_date__range=[start,end])
                                })
                                  # context=RequestContext(self.request))
        # response['Content-Type'] = 'text/plain; charset=utf-8'
        # response['Cache-Control'] = 'no-cache'
    
    
    # pdb.set_trace()
    return response

class ContactView(ListView):
    model = Contact
    template_name = 'general/contact.html' 

    def get_context_data(self, **kwargs):
        ctx = super(ContactView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx 


class FacultyInfoView(ListView):
    context_object_name= 'item_list'
    template_name = 'general/facultyinfo.html'   

    def get_queryset(self):
        return Faculty.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(FacultyInfoView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx  

# Authentication views here.
# def accountLoginView(request):
#     context= {}
#     context['program_list'] = Program.objects.all()
#     context.update(csrf(request))
#     return render_to_response('registration/login.html', context)


def accountAuthView(request):


    if request.user is not None:
        try:
            s = Student.objects.get(user=request.user.id)
            is_student = True
        except Student.DoesNotExist:
            is_student = False
        try:
            Faculty.objects.get(user=request.user.id)
            is_faculty = True
        except Faculty.DoesNotExist:
            is_faculty = False
        # pdb.set_trace()
        if is_student and request.user.registrationprofile.verified:
            return HttpResponseRedirect('/students')
        elif is_faculty and request.user.registrationprofile.verified:
            return HttpResponseRedirect('/faculty')

    return HttpResponseRedirect('/accounts/invalid/')
   
def myView(request):
    form = myForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    return render_to_response('my_template.html', {'form': form})
    

def accountInvalidView(request):
    context= {}
    context['program_list'] = Program.objects.all()
    context['error'] = True
    context.update(csrf(request))
    return render_to_response('general/account_invalid.html', context)

def accountLogoutView(request):
    auth.logout(request)
    return render_to_response('general/account_logout.html')


def accountRegisterView(request):

    if request.method == 'POST':
        student_form = ProfileForm(request.POST)
        faculty_form = FacultyForm(request.POST)
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='account'))
            return HttpResponseRedirect("/accounts/register_success")
    else:
        student_form = ProfileForm()
        faculty_form = FacultyForm()
    return render(request, "general/account_register.html", {
        'student_form': student_form, 'faculty_form': faculty_form,
    })


def accountRegisterSuccessView(request):
    return render_to_response('general/account_register_success.html')


