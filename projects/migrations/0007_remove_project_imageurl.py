# Generated by Django 4.2.7 on 2024-01-12 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_technology_technologyimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='imageURL',
        ),
    ]