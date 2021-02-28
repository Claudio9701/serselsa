from django.db import models
from django.urls import reverse 

# Create your models here.
class Cliente(models.Model):
    razon_social = models.CharField(max_length=100)
    ruc = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('cliente-detail', args=[str(self.id)])

class DiagramaMotor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    diagrama = models.ImageField(upload_to='diagramas', blank=True, null=True)

class Motor(models.Model):
    # Datos del motor
    marca = models.CharField(max_length=20, blank=True, null=True)
    numero_serie = models.CharField(max_length=20, blank=True, null=True)
    potencia = models.CharField(max_length=20, blank=True, null=True)
    voltaje_nominal = models.CharField(max_length=20, blank=True, null=True)
    corriente_nominal = models.CharField(max_length=20, blank=True, null=True)
    conexion = models.CharField(max_length=20, blank=True, null=True)
    rpm = models.CharField(max_length=20, blank=True, null=True)
    frecuencia = models.CharField(max_length=20, blank=True, null=True)
    aplicacion = models.CharField(max_length=20, blank=True, null=True)
    ranuras = models.CharField(max_length=20, blank=True, null=True)
    # Datos del bobinado
    pasos = models.CharField(max_length=20, blank=True, null=True)
    espiras = models.CharField(max_length=20, blank=True, null=True)
    calibre = models.CharField(max_length=20, blank=True, null=True)
    bob_en_serie = models.CharField(max_length=20, blank=True, null=True)
    peso_alambre= models.CharField(max_length=20, blank=True, null=True)
    grupos_de_bob = models.CharField(max_length=20, blank=True, null=True)
    tipo_conexion_del_bob = models.CharField(max_length=20, blank=True, null=True)
    altura_de_cab_de_bob_conexion = models.CharField(max_length=20, blank=True, null=True)
    salidas = models.CharField(max_length=20, blank=True, null=True)
    altura_de_cab_de_bob_posterior = models.CharField(max_length=20, blank=True, null=True)
    # Medidas del nucleo
    longitud_axial = models.CharField(max_length=20, blank=True, null=True)
    espesor_diente = models.CharField(max_length=20, blank=True, null=True)
    altura_ranura = models.CharField(max_length=20, blank=True, null=True)
    ancho_ranura = models.CharField(max_length=20, blank=True, null=True)
    profundiad_hierro_detras_ranura = models.CharField(max_length=20, blank=True, null=True)
    diametro_interno = models.CharField(max_length=20, blank=True, null=True)
    diametro_externo = models.CharField(max_length=20, blank=True, null=True)
    medida_eje_externo = models.CharField(max_length=20, blank=True, null=True)
    rodaje_delantero = models.CharField(max_length=20, blank=True, null=True)
    rodaje_posterior = models.CharField(max_length=20, blank=True, null=True)

    observaciones = models.TextField(blank=True, null=True)

    # Previas
    fases_choices = [('MF', 'Monofasico'), ('TF', 'Trifasico')]
    fases = models.CharField(max_length=2, choices=fases_choices, blank=True, null=True)
    diagrama = models.ForeignKey('DiagramaMotor', on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('motor-detail', args=[str(self.id)])

class Servicio(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    motor = models.ForeignKey('Motor', on_delete=models.CASCADE)
    mantenimiento_choices = [('PR', 'Preventivo'), ('CR', 'Correctivo')]
    mantenimiento = models.CharField(max_length=2, choices=mantenimiento_choices)
    observaciones = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('servicio-detail', args=[str(self.id)])
