# Generated by Django 3.1.7 on 2021-03-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_principle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principle',
            name='image',
            field=models.ImageField(default='django_schoolapp2_pro/django_schoolapp2_pro/static/nobody.jpg', upload_to=''),
        ),
    ]
