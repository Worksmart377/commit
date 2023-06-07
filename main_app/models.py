from django.db import models
from django.urls import reverse


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date = models.DateField('task due date')
    completed = models.BooleanField()
    project_name = models.ManyToOneRel(Project)
    journal_entry = models.ManyToManyRel(Journal)
    
    def __str__(self):
        return f'{self.get_name_display()} due on {self.date}'
    
    class Meta:
        ordering = ['date']
        
class Journal(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('journal entry date')
    entry = models.TextField(max_length=5000)
    project_name = models.ManyToOneRel(Project)
    task = models.ManyToManyField(Task)
    
    def __str__(self):
        return f'{self.get_entry_display()} was last edited on {self.date}'
    
    class Meta:
        ordering = ['-date']
        
class Video(models.Model):
    name = models.CharField(max_length=50) 
    url = models.URLField()     
    task_name = models.ManyToOneRel(Task)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    links = models.URLField(max_length=250)
    tasks = models.ManyToManyField(Task)
    youtube_tutorials = models.ManyToManyField(Video)
    journals = models.ManyToManyField(Journal)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})
    


