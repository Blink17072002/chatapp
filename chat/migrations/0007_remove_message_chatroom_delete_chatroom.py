# Generated by Django 4.2.1 on 2023-07-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_message_chatroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chatroom',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]
