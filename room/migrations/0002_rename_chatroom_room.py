# Generated by Django 4.2.1 on 2023-08-23 14:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatRoom',
            new_name='Room',
        ),
    ]