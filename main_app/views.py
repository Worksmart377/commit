from django.shortcuts import render, redirect
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})



def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    # generate a list of ids for all the tasks associated with each project
    
    # generate a list of tasks while excludes the ones containing ids included in the id_list

    # instantiate JournalForm to be rendered
    
    return render(request, 'projects/detail.html', {'project':project})
