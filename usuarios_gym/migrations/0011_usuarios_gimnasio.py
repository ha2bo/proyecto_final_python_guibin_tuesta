# Generated by Django 5.0.6 on 2024-06-23 17:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_gym', '0010_rename_usuarios_usuarios_contactados'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios_gimnasio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, null=True)),
                ('Telefono', models.CharField(max_length=100)),
                ('Mensaje', models.TextField(null=True)),
                ('sede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios_gym.sede')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
