from django.contrib import admin
from .models import Task

class TAdmin(admin.ModelAdmin):
    list_display= ('task', 'is_completed')
    search_fields= ('task',)


admin.site.register(Task, TAdmin)
