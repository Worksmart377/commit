from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here. 


class Journal(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('journal entry date')
    entry = models.TextField(max_length=5000)
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['-date'] 
        
class Task(models.Model):
    name = models.CharField(max_length=100, default='important task')
    description = models.TextField(max_length=300, default='detailed description')
    date = models.DateField('task due date', default='2023-12-30')
    completed = models.BooleanField(default=False)
    entries = models.ManyToManyField(Journal)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'task_id': self.id})
    
    class Meta:
        ordering = ['date']     

class Project(models.Model):
    name = models.CharField(max_length=100, default='very important project')
    technology = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    github = models.URLField(max_length=200, default='www.github.com')
    tasks = models.ManyToManyField(Task)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})
    


        

