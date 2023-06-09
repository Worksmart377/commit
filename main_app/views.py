from django.shortcuts import render, redirect
from .models import Project, Task, Journal, Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
from decouple import config

from django.views.generic import ListView, DetailView
# import google_auth_oauthlib.flow
# import googleapiclient.discovery
# import googleapiclient.errors

# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def about(request):
    # Include an .html file extension - unlike when rendering EJS templates (.ejs extension)
    return render(request, 'about.html')

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    # generate a list of ids for all the tasks associated with each task
    id_list = project.tasks.all().values_list('id') # [1, 3, 7]

    
    # generate a list of tasks while excludes the ones containing ids included in the id_list
    tasks_project_doesnt_have = Task.objects.exclude(id__in=id_list)

    # instantiate JournalForm to be rendered
    
    return render(request, 'projects/detail.html', {'project':project})

def tasks_index(request):
    tasks =  Task.objects.all()
    return render(request, 'tasks_index.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    # generate a list of ids for all the journals associated with each task
    id_list = task.entries.all().values_list('id') # [1, 3, 7]

    
    # generate a list of entries while excludes the ones containing ids included in the id_list
    entries_task_doesnt_have = Journal.objects.exclude(id__in=id_list)
    
    return render(request, 'tasks/task_detail.html', {'task':task})


class ProjectCreate (CreateView):
    model = Project
    fields = ['name', 'technology', 'description', 'github_link']
    # success_url = '/cats/' # not the preferred way 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskCreate (CreateView):
    model = Task
    fields = ['name', 'description', 'date', 'completed']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



API_KEY = config('API_KEY')


def configure():
    key= config('API_KEY')
    youtube = build('youtube', 'v3', developerKey=key)

    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q="coding",
        order= "date",
        type= 'video'
    )

    response = request.execute()

    print(response)
configure()
# def configure():
#     load_dotenv()
    
# def get_user_search(session, input):
#     url = f"https://www.googleapis.com/youtube/v3/searchq={input}&appid={os.getenv(api_key)}
# "


# scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# def main():
#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#     api_service_name = "youtube"
#     api_version = "v3"
#     client_secrets_file = "{load_dotenv}"

#     # Get credentials and create an API client
#     flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#         client_secrets_file, scopes)
#     credentials = flow.run_console()
#     youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, credentials=credentials)

#     request = youtube.search().list(
#         part="snippet",
#         maxResults=25,
#         q="coding"
#     )
#     response = request.execute()

#     print(response)

# if __name__ == "__main__":
#     main()