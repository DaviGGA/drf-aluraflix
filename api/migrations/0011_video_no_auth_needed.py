# Generated by Django 4.1.2 on 2022-11-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_category_user_remove_video_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='no_auth_needed',
            field=models.BooleanField(default=False),
        ),
    ]
