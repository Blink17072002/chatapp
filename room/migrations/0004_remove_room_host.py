# Generated by Django 4.2.1 on 2023-08-24 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_remove_room_created_remove_room_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
    ]
