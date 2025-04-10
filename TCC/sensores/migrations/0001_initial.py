# Generated by Django 4.2 on 2025-03-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logprevisaoia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_prevista', models.DateTimeField()),
                ('confianca', models.FloatField()),
                ('criada_em', models.DateTimeField(blank=True, null=True)),
                ('status_realizado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'LogPrevisaoIA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Previsaoia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_prevista', models.DateTimeField()),
                ('confianca', models.FloatField()),
            ],
            options={
                'db_table': 'PrevisaoIA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registrosinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinal', models.IntegerField()),
                ('data_hora', models.DateTimeField()),
            ],
            options={
                'db_table': 'RegistroSinal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Sensor',
                'managed': False,
            },
        ),
    ]
