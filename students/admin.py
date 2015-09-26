from django.contrib import admin
from students.models import *

class TimeTableInLine(admin.TabularInline):
	model = Time_Table
	extra = 1

class BatchAdmin(admin.ModelAdmin):
	inlines = [TimeTableInLine]

class TimeSlotInLine(admin.TabularInline):
	model = Time_Slot
	extra = 3

class SlotAdmin(admin.ModelAdmin):
	inlines = [TimeSlotInLine]


# Register your models here.
admin.site.register(Profile)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Notification)
admin.site.register(Question_Paper)
admin.site.register(Link)
admin.site.register(Book)
