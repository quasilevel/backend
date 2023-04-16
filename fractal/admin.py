from django.contrib import admin
from .models import task

@admin.register(task)
class useradmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'issue',
                     'created_at', 'completed_at', 'state', 'assignee',)
