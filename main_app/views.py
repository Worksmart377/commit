from django.shortcuts import render, redirect
from .models import Project, Task, Journal, Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
from decouple import config
from django.views.generic import ListView, DetailView
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from rest_framework.views import APIView
from rest_framework.response import Response
from oauth2_provider.decorators import protected_resource
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
import random
from django.http import JsonResponse



# Create your views here.

def random_class(pick):
    choices = ["table-primary", "table-secondary", "table-success", "table-danger", "table-warning", "table-info", "table-active"]
    pick = random.choice(choices)
    
    random_class(pick)

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(id=project_id)
    # id_list = tasks.project.all().values_list('id')
    # project_task_doesnt_have = Project.objects.exclude(id__in=id_list)
    
    
    return render(request, 'projects/detail.html', {'project':project, "tasks": tasks})



def tasks_index(request):
    tasks =  Task.objects.all()
    return render(request, 'tasks_index.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    id_list = task.entries.all().values_list('id') 
    entries_task_doesnt_have = Journal.objects.exclude(id__in=id_list)
    return render(request, 'tasks/task_detail.html', {'task':task})

# def assoc_task(request, project_id, task_id):
#     Project.objects.filter(id=project_id).tasks.add(task_id)
#     return redirect('task_list', project_id=project_id)

# def unassoc_task(request, project_id, task_id):
#     Project.objects.filter(id=project_id).tasks.remove(task_id)
#     return redirect('detail', project_id=project_id)


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

    
class ProjectCreate (CreateView):
    model = Project
    fields = ['name', 'technology', 'description', 'github']
    # success_url = '/cats/' # not the preferred way 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProjectUpdate(UpdateView):
    model = Project
    fields = "__all__"    
    
class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects/'
class TaskCreate (CreateView):
    model = Task
    fields = ['name', 'description', 'date', 'completed']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"  
    
class TaskDelete(DeleteView):
    model = Task
    success_url = '/tasks/'
    
class TaskList(ListView):
    model = Task


    
    
API_KEY = config('API_KEY')

def search_results(request):
    searched = request.GET.get('searched', '')  
    if searched:
        # Perform the search
        key = config('API_KEY')
        youtube = build('youtube', 'v3', developerKey=key)
        request = youtube.search().list(
            part="snippet",
            maxResults=5,
            q=searched,
            order="date",
            type='video'
        )

        results = request.execute()
        # results_json = results.JsonResponse()
        # results_json.content

        print(results)
        return render(request, 'search/results.html', {'results': results})
    else:
        return render(request, 'search/results.html', {'results': {}})

