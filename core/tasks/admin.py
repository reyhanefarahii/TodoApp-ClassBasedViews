from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'status', 'created_at', 'updated_at')
    list_display=('user', 'title', 'status', 'created_at', 'updated_at')
    list_filter = ('status','user')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Task,TaskAdmin)