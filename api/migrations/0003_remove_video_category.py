# Generated by Django 4.1.2 on 2022-11-02 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_video_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='category',
        ),
    ]
