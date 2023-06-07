from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('projects/<int:project_id>/', views.projects_detail, name='detail'),
        path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),

        

]