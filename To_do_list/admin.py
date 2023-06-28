from django.contrib import admin
from To_do_list.models import Task, Status


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'start_date', 'date_of_completion']
    list_filter = ['start_date', 'date_of_completion']
    search_fields = ['description']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
# Register your models here.
