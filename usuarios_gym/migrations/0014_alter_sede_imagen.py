# Generated by Django 5.0.6 on 2024-06-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_gym', '0013_usuarios_gimnasio_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='sedes'),
        ),
    ]