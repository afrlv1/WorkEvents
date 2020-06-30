# Generated by Django 3.0.7 on 2020-06-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('title', models.CharField(blank=True, help_text='Title', max_length=255, null=True, verbose_name='Title')),
                ('body', models.TextField(blank=True, help_text='Textual Event', null=True, verbose_name='Textual Event')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
    ]
