# Generated by Django 4.1.2 on 2022-11-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_video_user_alter_category_title_alter_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
