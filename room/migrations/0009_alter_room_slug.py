# Generated by Django 4.2.1 on 2023-08-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_alter_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, default=True, null=True),
        ),
    ]
