from django.contrib import admin
from students.models import *
from general.models import Student

class TimeTableInLine(admin.TabularInline):
	model = Time_Table
	extra = 1

class SubjectInLine(admin.TabularInline):
	model = Subject
	extra = 1

class BatchAdmin(admin.ModelAdmin):
	inlines = [TimeTableInLine, SubjectInLine]

class TimeSlotInLine(admin.TabularInline):
	model = Time_Slot
	extra = 3

class SlotAdmin(admin.ModelAdmin):
	inlines = [TimeSlotInLine]

class StudentAdmin(admin.ModelAdmin):
	list_display = ('user', 'activation_key_expired','verified')

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Slot, SlotAdmin)
# admin.site.register(Notification)
admin.site.register(Question_Paper)
admin.site.register(Link)
admin.site.register(Book)
# admin.site.register(Subject)