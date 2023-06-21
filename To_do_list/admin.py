from django.contrib import admin
from To_do_list.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'start_date', 'date_of_completion']
    list_filter = ['start_date', 'date_of_completion']
    search_fields = ['description']


admin.site.register(Task, TaskAdmin)
# Register your models here.
