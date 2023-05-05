from django.contrib import admin
from .models import task

@admin.register(task)
class useradmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'issue',
                     'created_at', 'completed_at', 'state', 'assignees_display',)
    def assignees_display(self,obj):
        return ",".join([str(assignee) for assignee in obj.assignee.all()])
    assignees_display.short_description='Assignees'
