from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='usuarios_gym/static/images/', null=True, blank=True)
    tipo_gimnasio = models.CharField(
        max_length=10,
        choices=[
            ('prime', 'Prime'),
            ('plus', 'Plus'),
            ('classic', 'Classic'),
        ], null= True)

    def __str__(self):
        return self.nombre
    

class usuarios_contactados(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(null=True)
    Telefono = models.CharField(max_length=100)
    Mensaje = models.TextField(null=True)
#    user_id = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.correo}" 
    


class usuarios_gimnasio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(null=True)
    Telefono = models.CharField(max_length=100, null= True)
    user_id = models.OneToOneField(User, on_delete= models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.sede}" 