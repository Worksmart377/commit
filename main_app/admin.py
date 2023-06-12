from django.contrib import admin

from .models import Task, Project, Journal

admin.site.register([Project, Journal, Task])
# Register your models here.
