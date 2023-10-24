from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=60)
    logo= models.ImageField()

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    TIPO_CHOICES=[
        ("S", "Suspension de actividad"),
        ("C", "Suspension de clase"),
        ("I", "Informacion"),
    ]

    id= models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=150)
    detalle= models.CharField(max_length=1000)
    detalle_corto= models.CharField(max_length=200)
    tipo= models.CharField(max_length=1, choices=TIPO_CHOICES)
    entidad= models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible= models.BooleanField()
    fecha_publicacion= models.DateTimeField()
    publicado_por= models.ForeignKey(User,related_name="publicaciones" ,on_delete=models.CASCADE)
    modificado_por= models.ForeignKey(User,related_name="modificaciones" ,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


