# Generated by Django 4.2.9 on 2024-04-13 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Genres", "0005_youtubechannel_video_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="youtubechannel", name="video_name",),
    ]
