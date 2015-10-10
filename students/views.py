from django.http import HttpResponse
from general.models import *
from students.models import *
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

# from django.core.context_processors import csrf
# from django.template import RequestContext,loader
# from django.views import generic
# from django.utils import timezone
from django.shortcuts import render, render_to_response

class HomeView(ListView):
    model = Program
    template_name = 'general/account-index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()
        ctx['news_list'] = News.objects.order_by('-pub_date')[:5]
        ctx['notification_list']= Notification.objects.order_by('-pub_date')[:5]

        
        return ctx

class ProgramView(ListView):
    model = Program
    template_name = 'general/account-program.html'

    def get_queryset(self):
        return Program.objects.all()


# @login_required
class ProgramDetailView(SingleObjectMixin, ListView):
    
    template_name = "general/account-programdetail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Program.objects.all())
        return super(ProgramDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(ProgramDetailView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx
    def get_queryset(self):
        return self.object.course_set.all()

# @login_required
class NewsView(ListView):
    model = News
    template_name = 'general/account-news.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx


    
# @login_required
class NotificationView(ListView):
    model = Notification
    template_name = 'general/account-notification.html'

    
    def get_context_data(self, **kwargs):
        ctx = super(NotificationView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx

# @login_required
class ContactView(ListView):
    model = Contact
    template_name = 'general/account-contact.html' 

    def get_context_data(self, **kwargs):
        ctx = super(ContactView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx 

# @login_required
class FacultyInfoView(ListView):
    context_object_name= 'item_list'
    template_name = 'faculty/account-facultyinfo.html'   

    def get_queryset(self):
        return Faculty.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(FacultyInfoView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx  


# @login_required
def FacultyView(request):
    context= {}
    context['program_list'] = Program.objects.all()
    context['time_slot_list'] = Time_Slot.objects.all()
    context['notification_list'] = Notification.objects.all().order_by('-pub_date')[:5]
    context['user']=request.user
    # time table lists
    
    days = ['monday','tuesday','wednessday','thursday','friday','saturday']
    day_number = 0
    for day in days:
        context[day] = []
        day_number += 1
        time_table = request.user.faculty.faculty_time_table_set.filter(Day=day_number)
        for time in Time_Slot.objects.all():
            for item in time_table:
                if item.Time_Slot == time:
                    context[day].append(item)
                    break
            else:
                context[day].append('-')
    return render_to_response('faculty/bulletin.html', context)

    #context['profile']=request.user.profile #Profile.objects.get('User'=request__user)#request.user.profile
    
@login_required
def StudentView(request):
    context= {}
    context['program_list'] = Program.objects.all()
    context['time_slot_list'] = Time_Slot.objects.all()
    context['notification_list'] = Notification.objects.all().order_by('-pub_date')[:5]
    context['user']=request.user
    # time table lists
    
    days = ['monday','tuesday','wednessday','thursday','friday','saturday']
    day_number = 0
    for day in days:
        context[day] = []
        day_number += 1
        time_table = request.user.profile.Batch.time_table_set.filter(Day=day_number)
        for time in request.user.profile.Batch.Slot.time_slot_set.all():
            for item in time_table:
                if item.Time_Slot == time:
                    context[day].append(item)
                    break
            else:
                context[day].append('-')
    return render_to_response('students/bulletin.html', context)

    #context['profile']=request.user.profile #Profile.objects.get('User'=request__user)#request.user.profile
    

    



def ShelfView(request):
    context= {}
    context['program_list'] = Program.objects.all()
    context['user']=request.user
    context['profile']=request.user.profile #Profile.objects.get('User'=request__user)#request.user.profile
    context['book_list'] = Book.objects.all()
    context['question_paper_list'] = Question_Paper.objects.all()
    context['link_list'] = Link.objects.all()
    
    return render_to_response('students/shelf.html', context)

def ProfileView(request):
    context= {}
    context['program_list'] = Program.objects.all()
    context['user']=request.user
    context['profile']=request.user.profile #Profile.objects.get('User'=request__user)#request.user.profile
    
    return render_to_response('students/profile.html', context)

def ChatroomView(request):
    context= {}
    context['program_list'] = Program.objects.all()
    context['user']=request.user
    context['profile']=request.user.profile #Profile.objects.get('User'=request__user)#request.user.profile
    
    return render_to_response('students/classroom.html', context)

class EditProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'students/edit-profile.html'

    def get(self, request, **kwargs):
        self.object = Profile.objects.get(User = User.objects.get(id=self.kwargs['id']))
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Profile.objects.get(User = User.objects.get(id=self.kwargs['id']))
        return obj