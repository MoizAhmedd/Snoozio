# Generated by Django 2.2 on 2019-05-08 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SnoozioApp', '0013_sleeptimes_end_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sleeptimes',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='sleeptimes',
            name='start_time',
        ),
    ]
