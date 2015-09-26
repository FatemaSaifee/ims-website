from django.conf.urls import patterns, include, url
from general import views
from django.views.generic import ListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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

)

urlpatterns += staticfiles_urlpatterns()