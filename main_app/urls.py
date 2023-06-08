from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('tasks_index', views.tasks_index, name='tasks_index'),
        path('projects/<int:project_id>/', views.projects_detail, name='detail'),
        path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
        path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),

        

]