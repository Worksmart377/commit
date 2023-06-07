from django.contrib import admin

from .models import Task, Project, Journal, Video

admin.site.register([Project, Journal, Task, Video])
# Register your models here.
