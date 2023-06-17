from django.contrib import admin
from To_do_list.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_of_completion']
    list_filter = ['date_of_completion']
    search_fields = ['description']


admin.site.register(Task, TaskAdmin)
# Register your models here.
