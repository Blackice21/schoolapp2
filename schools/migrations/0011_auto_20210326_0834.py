# Generated by Django 3.1.7 on 2021-03-26 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_school_principle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='principle',
            name='image',
        ),
        migrations.RemoveField(
            model_name='school',
            name='principle',
        ),
    ]
