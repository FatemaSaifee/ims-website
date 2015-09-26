from django.http import HttpResponse
from general.models import Program, Course
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