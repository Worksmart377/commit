# Generated by Django 4.2.1 on 2023-06-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_alter_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
