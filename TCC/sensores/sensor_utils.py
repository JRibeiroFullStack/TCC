# sensores/sensor_utils.py
from sensores.models import Logprevisaoia, Previsaoia, Registrosinal, Sensor
from datetime import datetime

'''# Função para salvar dados na tabela Logprevisaoia
def salvar_log_previsaoia(sensor_nome, confianca, status_realizado=None):
    try:
        # Verifica se o sensor existe no banco
        sensor = Sensor.objects.get(nome=sensor_nome)
        
        # Cria um log com a data/hora atual
        data_hora_prevista = datetime.now()
        log = Logprevisaoia(
            sensor=sensor,
            data_hora_prevista=data_hora_prevista,
            confianca=confianca,
            status_realizado=status_realizado,
            criada_em=datetime.now()
        )
        log.save()
        print(f"Log de previsão inserido para o sensor {sensor_nome}")
    except Sensor.DoesNotExist:
        print(f"Sensor {sensor_nome} não encontrado")

# Função para salvar dados na tabela Previsaoia
def salvar_previsaoia(sensor_nome, confianca):
    try:
        # Verifica se o sensor existe no banco
        sensor = Sensor.objects.get(nome=sensor_nome)
        
        # Cria uma previsão com a data/hora atual
        data_hora_prevista = datetime.now()
        previsao = Previsaoia(
            sensor=sensor,
            data_hora_prevista=data_hora_prevista,
            confianca=confianca
        )
        previsao.save()
        print(f"Previsão inserida para o sensor {sensor_nome}")
    except Sensor.DoesNotExist:
        print(f"Sensor {sensor_nome} não encontrado")'''

# Função para salvar dados na tabela Registrosinal
def salvar_registro_sinal(sensor_nome, sinal):
    try:
        # Verifica se o sensor existe no banco
        sensor = Sensor.objects.get(nome=sensor_nome)
        
        # Cria um registro com a data/hora atual
        data_hora = datetime.now()
        registro = Registrosinal(
            sensor=sensor,
            sinal=sinal,
            data_hora=data_hora
        )
        registro.save()
        print(f"Registro de sinal inserido para o sensor {sensor_nome}")
    except Sensor.DoesNotExist:
        print(f"Sensor {sensor_nome} não encontrado")
