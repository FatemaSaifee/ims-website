from django.conf.urls import patterns, include, url
from faculty import views
#from django.views.generic import ListView


urlpatterns = patterns('',
	url(r'^$', views.FacultyView, name='bulletin'),
	#url(r'^bulletin/(?P<pk>\d+)/$', views.BulletinView.as_view(), name='bulletin'),
	url(r'^profile/$', views.ProfileView, name='profile'),
	url(r'^profile/edit/(?P<id>\d+)/$', views.EditFacultyView.as_view(), name='edit-profile'),
	url(r'^shelf/$', views.ShelfView, name='shelf'),
	# url(r'^chatroom/$', views.ChatroomView, name='chatroom'),
	# url(r'^chat/', include('chatrooms.urls', namespace='chatroom')),
	
)