from django.shortcuts import render
from django.http import HttpResponseRedirect
from general.models import *
from faculty.models import *
from django.template import RequestContext,loader
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from students.models import ProfileForm

from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

from django.core.context_processors import csrf
from django.shortcuts import render_to_response


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

class ProgramView(ListView):
    model = Program
    template_name = 'general/program.html'

    def get_queryset(self):
        return Program.objects.all()



class ProgramDetailView(SingleObjectMixin, ListView):
    
    template_name = "general/programdetail.html"

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

class NewsView(ListView):
    model = News
    template_name = 'general/news.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx


    

class NotificationView(ListView):
    model = Notification
    template_name = 'general/notification.html'

    
    def get_context_data(self, **kwargs):
        ctx = super(NotificationView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx

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
    template_name = 'faculty/facultyinfo.html'   

    def get_queryset(self):
        return Faculty.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(FacultyInfoView, self).get_context_data(**kwargs)
        ctx['program_list'] = Program.objects.all()
        ctx['course_list'] = Course.objects.all()

        return ctx  

# Authentication views here.
def accountLoginView(request):
    context= {}
    context['program_list'] = Program.objects.all()
    context.update(csrf(request))
    return render_to_response('general/account_login.html', context)

def accountAuthView(request):
    username = request.POST.get('username','')
    #group = request.POST.get('group','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    context= {}
    context['err'] = ['bv nb m']
    if user is not None:
        for group in user.groups.values_list('name',flat=True):
            if group == 'staff':
                auth.login(request, user)
                return HttpResponseRedirect('/staff')
            elif group == 'student':
                auth.login(request, user)
                return HttpResponseRedirect('/students')
            elif group == 'faculty':
                auth.login(request, user)
                return HttpResponseRedirect('/faculty')
    return HttpResponseRedirect('/accounts/invalid/')
    #         else :
    #             return HttpResponseRedirect('/accounts/invalid')
    #     return HttpResponseRedirect('/accounts/invalid')
    # else :
    #     return HttpResponseRedirect('/accounts/invalid')
    ###################################################
    # if user.groups.filter(name=group).exists():
    #     auth.login(request, user)
    #     return HttpResponseRedirect('/account')
    # else:
    #     return HttpResponseRedirect('/account/invalid')
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

        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='account'))
            return HttpResponseRedirect("/accounts/register_success")
    else:
        form = ProfileForm()
    return render(request, "general/account_register.html", {
        'form': form,
    })


def accountRegisterSuccessView(request):
    return render_to_response('general/account_register_success.html')


