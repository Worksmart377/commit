from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('projects/<int:project_id>/', views.projects_detail, name='detail'),
        

]