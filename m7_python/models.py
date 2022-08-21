from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
  id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

class Tipo_inmueble(models.Model):
  tipo_inmueble = models.TextField()

class Comuna(models.Model):
  comuna = models.CharField(max_length = 40)
  def __str__(self):
    return self.comuna
    
class Region(models.Model):
  region = models.CharField(max_length = 80)

class Tipo_user(models.Model):
  tipo_user = models.CharField(max_length = 40)

class Profile(models.Model):
  user = models.OneToOneField(to=User, on_delete=models.CASCADE)
  id_tipo_user = models.ForeignKey(to=Tipo_user, on_delete=models.CASCADE, null=True)
  rut = models.CharField(max_length = 40)
  direccion = models.CharField(max_length = 40)
  telefono = models.CharField(max_length = 40)
  correo = models.EmailField()

class Inmuebles(models.Model):
  id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
  id_tipo_inmueble = models.ForeignKey(to=Tipo_inmueble, on_delete=models.CASCADE, null=True)
  id_comuna = models.ForeignKey(to=Comuna, on_delete=models.CASCADE, null=True)
  id_region = models.ForeignKey(to=Region, on_delete=models.CASCADE, null=True)
  nombre_inmueble = models.CharField(max_length = 200)
  descripcion = models.TextField()
  m2_construido = models.FloatField()
  m2_terreno = models.FloatField()
  numero_banos = models.IntegerField(default=0)
  numero_est = models.IntegerField()
  numero_hab = models.IntegerField(default=0)
  direccion = models.CharField(max_length = 40)

class SolicitudInmueble(models.Model):
  id_user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_inmueble = models.ForeignKey(Inmuebles, on_delete=models.CASCADE)
