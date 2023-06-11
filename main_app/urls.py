from django.urls import path
from . import views

urlpatterns = [
        path('index/', views.index, name='index'),
        path('', views.about, name='about'),
        path('accounts/signup/', views.signup, name='signup'),
        path('search', views.search_results, name='search_results'),
        path('search/', views.video_query, name='search_detail'),
        path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
        path('projects/<int:project_id>/', views.projects_detail, name='detail'),
        path('projecs/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
        path('projecs/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
        path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
        path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
        path('journals/<int:pk>/update/', views.EntryUpdate.as_view(), name='entry_update'),
        path('journals/<int:pk>/delete/', views.EntryDelete.as_view(), name='entry_delete'),
        path('tasks/', views.TaskList.as_view(), name='tasks_list'),
        path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
        path('tasks/create/', views.TaskCreate.as_view(), name='task_create'),

        

]