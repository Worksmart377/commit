from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('results', views.search_results, name='search_results'),
        path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
        path('projects/<int:project_id>/', views.projects_detail, name='detail'),
        path('projecs/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
        path('projecs/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
        path('tasks/', views.TaskList.as_view(), name='tasks_list'),
        # path('project/<int:project_id>/assoc_task/<int:task_id>/', views.assoc_task, name='assoc_task'),
        path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
        path('tasks/create/', views.TaskCreate.as_view(), name='task_create'),

        

]