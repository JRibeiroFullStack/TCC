from django.db import models


class Logprevisaoia(models.Model):
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING)
    data_hora_prevista = models.DateTimeField()
    confianca = models.FloatField()
    criada_em = models.DateTimeField(blank=True, null=True)
    status_realizado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LogPrevisaoIA'


class Previsaoia(models.Model):
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING)
    data_hora_prevista = models.DateTimeField()
    confianca = models.FloatField()

    class Meta:
        managed = False
        db_table = 'PrevisaoIA'


class Registrosinal(models.Model):
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING)
    sinal = models.IntegerField()
    data_hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'RegistroSinal'


class Sensor(models.Model):
    nome = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'Sensor'
