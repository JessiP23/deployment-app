# Generated by Django 4.2.7 on 2024-01-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_imageurl_imagerendering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imageURL',
            field=models.ImageField(blank=True, upload_to='projects/project_images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.ImageField(blank=True, upload_to='projects/project_images'),
        ),
    ]
