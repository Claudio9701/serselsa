# Generated by Django 3.1.3 on 2020-11-06 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('ruc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DiagramaMotor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('diagrama', models.ImageField(upload_to='diagramas')),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fases', models.CharField(choices=[('MF', 'Monofasico'), ('TF', 'Trifasico')], max_length=2)),
                ('diagrama', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.diagramamotor')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mantenimiento', models.CharField(choices=[('PR', 'Preventivo'), ('CR', 'Correctivo')], max_length=2)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.motor')),
            ],
        ),
    ]
