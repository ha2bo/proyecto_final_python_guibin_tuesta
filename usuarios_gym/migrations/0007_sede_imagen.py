# Generated by Django 5.0.6 on 2024-06-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_gym', '0006_remove_sede_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='sede',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios_gym/static/images/'),
        ),
    ]