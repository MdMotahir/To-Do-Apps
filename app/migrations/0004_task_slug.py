# Generated by Django 3.1.7 on 2021-02-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_task_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
