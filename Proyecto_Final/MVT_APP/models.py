from django.db import models
from django.contrib.auth.models import User


class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_Publicacion = models.DateField() 
    genero = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    calificacion = models.IntegerField()

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    email = models.EmailField()
    nacionalidad = models.CharField(max_length=50)

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    pais = models.CharField(max_length=50)
    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
