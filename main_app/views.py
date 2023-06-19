from django.shortcuts import render, redirect
from .models import Project, Task, Journal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from googleapiclient.discovery import build
import os

from decouple import config
from django.views.generic import ListView, DetailView
import random
from django.contrib.auth.forms import UserCreationForm
from .forms import JournalForm
from django.urls import reverse_lazy


# Create your views here.

def random_class(pick):
    choices = ["table-primary", "table-secondary", "table-success", "table-danger", "table-warning", "table-info", "table-active"]
    pick = random.choice(choices)
    
    random_class(pick)

def index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'index.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')

@login_required
def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    id_list = project.tasks.all().values_list('id') 
    tasks = project.tasks.all()
    tasks_project_doesnt_have = Task.objects.exclude(id__in=id_list)
    return render(request, 'projects/detail.html', 
    {
        'project': project,
        'tasks': tasks,
        'not_tasks': tasks_project_doesnt_have,
    })
    
@login_required
def assoc_task(request, project_id, task_id):
    Project.objects.get(id=project_id).tasks.add(task_id)
    return redirect('detail', project_id=project_id)

@login_required
def unassoc_task(request, project_id, task_id):
    Project.objects.get(id=project_id).tasks.remove(task_id)
    return redirect('detail', project_id=project_id)


    
    
@login_required
def tasks_index(request):
    tasks =  Task.objects.all()
    return render(request, 'tasks_index.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    id_list = task.entries.all().values_list('id') 
    entries_task_does_have = Journal.objects.filter(id__in=id_list)
    journal_form = JournalForm()
    print(task)
    return render(request, 'tasks/task_detail.html', {
    'task': task,
    'id_list': id_list,         
    'journal_form': journal_form,
    'entries':entries_task_does_have
})

@login_required
def entry_detail(request, entry_id):
    entry = Journal.objects.get(id=entry_id)
    return render(request, 'journals/entry_detail.html', {
    'entry':entry,         
})
    
@login_required
def add_entry(request, task_id):
    form = JournalForm(request.POST)

    # validate the form
    if form.is_valid():
        new_entry = form.save(commit=False)
        new_entry.task_id = task_id
        '''
        {
            title: 'lovely entry',
            date: '2023-06-11',
            task_id: 1
        }
        '''
        new_entry.save()
    return redirect('task_detail', task_id=task_id)

@login_required
def assoc_entry(request, task_id, entry_id):
    Task.objects.get(id=task_id).entries.add(entry_id)
    return redirect('detail', task_id=task_id)

@login_required
def unassoc_entry(request, task_id, entry_id):
    Task.objects.get(id=task_id).entries.remove(entry_id)
    return redirect('detail', task_id=task_id)



def signup(request):
    # POST request
    error_message = ''
        # user is signing up with a form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        else:
            error_message = 'invalid signup - try again'
    # GET request
        # user is navigating to signup page to fill out form
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
    
    })
    
class CustomLoginView(LoginView):
    template_name = 'main_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('')
    
    
class ProjectCreate (LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'technology', 'description', 'github']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'technology', 'description', 'github', 'tasks']    
    
class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/index'
class TaskCreate (LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'date', 'completed']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'date', 'completed'] 
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/tasks/'
    
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    
class EntryCreate (LoginRequiredMixin, CreateView):
    model = Journal
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    fields = "__all__"  
    
class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    success_url = '/journals/'
    
class EntryList(LoginRequiredMixin, ListView):
    model = Journal


    
    
API_KEY = config('API_KEY')

def search_results(request):
    searched = request.GET.get('searched', '')  
    if searched:
        # Perform the search
        key = config('API_KEY')
        youtube = build('youtube', 'v3', developerKey=key)
        query = youtube.search().list(
            part="snippet",
            maxResults=12,
            q=searched,
            order="date",
            type='video'
        )

        results = query.execute()

        print(results)
        return render(request, 'search/results.html', {'results': results})
    else:
        return render(request, 'search/results.html', {'results': {}})

        
