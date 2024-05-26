from django.contrib import admin
from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'skills', 'ending_date')
    search_fields = ('title', 'skills')

# Register your models here.
admin.site.register(Job, JobAdmin)