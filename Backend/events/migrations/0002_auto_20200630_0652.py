# Generated by Django 3.0.7 on 2020-06-30 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='day',
            new_name='day_event',
        ),
    ]
