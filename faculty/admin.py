from django.contrib import admin
from faculty.models import *

# Register your models here.

class TimeTableInLine(admin.TabularInline):
	model = Faculty_Time_Table
	extra = 1

class FacultyAdmin(admin.ModelAdmin):
	inlines = [TimeTableInLine]

admin.site.register(Faculty, FacultyAdmin)

