# Generated by Django 3.1.7 on 2021-03-05 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0007_auto_20210305_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='principle',
            name='image',
        ),
    ]