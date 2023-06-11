# Generated by Django 4.2.1 on 2023-06-11 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_project_tasks_task_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journal',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='channel_title',
            field=models.CharField(default='great channel'),
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.CharField(default='great description'),
        ),
        migrations.AddField(
            model_name='video',
            name='published_at',
            field=models.DateTimeField(default='2023-06-11'),
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnails_default',
            field=models.URLField(default='youtube.com'),
        ),
    ]
