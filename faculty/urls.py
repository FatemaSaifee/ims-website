from django.conf.urls import patterns, include, url
from faculty import views
from django.contrib.auth.decorators import login_required
#from django.views.generic import ListView


urlpatterns = patterns('',
	url(r'^$', views.FacultyView, name='bulletin'),
	#url(r'^bulletin/(?P<pk>\d+)/$', views.BulletinView.as_view(), name='bulletin'),
	url(r'^profile/$', views.ProfileView, name='profile'),
	url(r'^profile/edit/(?P<id>\d+)/$', login_required(views.EditFacultyView.as_view()), name='edit-profile'),
	url(r'^shelf/$', views.ShelfView, name='shelf'),
	url(r'^program/$', login_required(views.ProgramView.as_view()), name='program'),
	url(r'^program/(?P<pk>\d+)/$', login_required(views.ProgramDetailView.as_view()), name='programdetail'),
	url(r'^news/$', login_required(views.NewsView.as_view()), name='news'),
	url(r'^notification/$', login_required(views.NotificationView.as_view()), name='notification'),
	url(r'^contact/$', login_required(views.ContactView.as_view()), name='contact'),
	url(r'^faculty_info/$', login_required(views.FacultyInfoView.as_view()), name='facultyinfo'),
	# url(r'^chatroom/$', views.ChatroomView, name='chatroom'),
	# url(r'^chat/', include('chatrooms.urls', namespace='chatroom')),
	
)