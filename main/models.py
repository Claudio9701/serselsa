from django.db import models

# Create your models here.
class Cliente(models.Model):
    razon_social = models.CharField(max_length=100)
    ruc = models.IntegerField()

class DiagramaMotor(models.Model):
    nombre = models.CharField(max_length=100)
    diagrama = models.ImageField(upload_to='diagramas')

class Motor(models.Model):
    fases_choices = [('MF', 'Monofasico'), ('TF', 'Trifasico')]
    fases = models.CharField(max_length=2, choices=fases_choices)
    diagrama = models.ForeignKey('DiagramaMotor', on_delete=models.SET_NULL, null=True, blank=True)

class Servicio(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    motor = models.ForeignKey('Motor', on_delete=models.CASCADE)
    mantenimiento_choices = [('PR', 'Preventivo'), ('CR', 'Correctivo')]
    mantenimiento = models.CharField(max_length=2, choices=mantenimiento_choices)
    observaciones = models.TextField(blank=True, null=True)
