# Generated by Django 3.1.7 on 2021-03-26 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0018_remove_school_principle'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='principle',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.principle'),
        ),
    ]
