from django.conf.urls import patterns, include, url
from general import views
from django.views.generic import ListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^program/$', views.ProgramView.as_view(), name='program'),
	url(r'^program/(?P<pk>\d+)/$', views.ProgramDetailView.as_view(), name='programdetail'),
	url(r'^news/$', views.NewsView.as_view(), name='news'),
	url(r'^notification/$', views.NotificationView.as_view(), name='notification'),
	url(r'^contact/$', views.ContactView.as_view(), name='contact'),
	url(r'^faculty_info/$', views.FacultyInfoView.as_view(), name='facultyinfo'),
	url(r'^accounts/register/$', views.accountRegisterView, name='accountregister'),
    url(r'^accounts/register_success/$', views.accountRegisterSuccessView, name='accountregistersuccess'),
    url(r'^accounts/login/$', views.accountLoginView, name='accountlogin'),
    url(r'^accounts/logout/$', views.accountLogoutView, name='accountlogout'),
    url(r'^accounts/auth/$', views.accountAuthView, name='accountauth'),
    url(r'^accounts/invalid/$', views.accountInvalidView, name='accountinvalid'),
	url(r'^accounts/$', login_required(views.Account_HomeView.as_view()), name='accounthome'),
    url(r'^accounts/program/$', login_required(views.AccountProgramView.as_view()), name='accountprogram'),
	url(r'^accounts/program/(?P<pk>\d+)/$', login_required(views.AccountProgramDetailView.as_view()), name='accountprogramdetail'),
	url(r'^accounts/news/$', login_required(views.AccountNewsView.as_view()), name='news'),
	url(r'^accounts/notification/$', login_required(views.AccountNotificationView.as_view()), name='accountnotification'),
	url(r'^accounts/contact/$', login_required(views.AccountContactView.as_view()), name='accountcontact'),
	url(r'^accounts/faculty_info/$', login_required(views.AccountFacultyInfoView.as_view()), name='accountfacultyinfo'),

)

urlpatterns += staticfiles_urlpatterns()