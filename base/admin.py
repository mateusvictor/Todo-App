from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'title', 'description', 'complete')
	fields = ['id', 'user', 'title', 'description', 'complete']
