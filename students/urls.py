from django.conf.urls import patterns, include, url
from students import views
#from django.views.generic import ListView


urlpatterns = patterns('',
	url(r'^$', views.StudentView, name='bulletin'),
	#url(r'^bulletin/(?P<pk>\d+)/$', views.BulletinView.as_view(), name='bulletin'),
	url(r'^profile/$', views.ProfileView, name='profile'),
	url(r'^profile/edit/(?P<id>\d+)/$', views.EditProfileView.as_view(), name='edit-profile'),
	url(r'^shelf/$', views.ShelfView, name='shelf'),
	url(r'^program/$', views.ProgramView.as_view(), name='program'),
	url(r'^program/(?P<pk>\d+)/$', views.ProgramDetailView.as_view(), name='programdetail'),
	url(r'^news/$', views.NewsView.as_view(), name='news'),
	url(r'^notification/$', views.NotificationView.as_view(), name='notification'),
	url(r'^contact/$', views.ContactView.as_view(), name='contact'),
	url(r'^faculty_info/$', views.FacultyInfoView.as_view(), name='facultyinfo'),
	# url(r'^chatroom/$', views.ChatroomView, name='chatroom'),
	# url(r'^chat/', include('chatrooms.urls', namespace='chatroom')),
	
)