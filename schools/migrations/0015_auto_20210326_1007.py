# Generated by Django 3.1.7 on 2021-03-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0014_auto_20210326_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principle',
            name='image',
            field=models.ImageField(default='nobody.jpg', upload_to='media'),
        ),
    ]
