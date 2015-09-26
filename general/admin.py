from django.contrib import admin
from general.models import * 
#from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline 
#from example.models import *

# from django.db.models.loading import cache as model_cache
#if not model_cache.loaded:
#   model_cache.get_models()

# Register your models here 
class NewsAdmin(admin.ModelAdmin):
	list_display = ('Title','pub_date')
	list_filter = ['pub_date']

class NotificationAdmin(admin.ModelAdmin):
	list_display = ('Title','pub_date')
	list_filter = ['pub_date']


class CourseInLine(admin.StackedInline):
	model = Course
	extra = 1


class ProgramAdmin(admin.ModelAdmin):
	inlines = [CourseInLine]


class CourseAdmin(admin.ModelAdmin):
	##if we want to decide order of fields in the admin form
	#fields = ['course_name','number_of_semester']
	list_display = ('course_name','program_name','number_of_semester')
	
	list_filter = ['number_of_semester']
	search_fields = ['course_name','program_name']

	fieldsets = [
		(None,		{'fields': ['course_name','program_name','number_of_semester']}),
		('About course',{'fields': ['description','objective','learning_outcomes'], 'classes':['collapse']}),
	]

class ContactAdmin(admin.ModelAdmin):
	list_display = ('Heading','Description')


admin.site.register(Program, ProgramAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Contact,ContactAdmin)
#admin.site.register(Student)

#admin.site.register(Course)


