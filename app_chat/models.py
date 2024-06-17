from django.db import models

# Create your models here.
class Carreras(models.Model):
    nombre = models.CharField(max_length=80)
    status = models.SmallIntegerField()

class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    ap_pat = models.CharField(max_length=80)
    ap_mat = models.CharField(max_length=80)
    usu = models.CharField(max_length=20)
    passw = models.CharField(max_length=12)
    fecha_nac = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carreras,on_delete=models.PROTECT)
    #carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    status = models.SmallIntegerField()

class Mensajes(models.Model):
    txt_mensaje = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona,on_delete=models.PROTECT)
    status = models.SmallIntegerField()