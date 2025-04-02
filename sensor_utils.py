from datetime import datetime
import time
from unittest.mock import MagicMock
from sensores.models import Sensor, Registrosinal

def get_or_create_sensor(sensor_nome):
    sensor, created = Sensor.objects.get_or_create(
                        nome=sensor_nome
                      )
    return sensor


# Simulação de sensor (para testes)
def simula_sensor(SENSOR_PIN, estado):
    SENSOR_PIN.is_pressed = estado == "HIGH"

# Salva os dados no banco em vez de JSON
def salvar_dados_no_banco(sensor_nome, estado):
    timestamp = datetime.now()
    Registrosinal.objects.create(
        nome=sensor_nome,
        estado=estado,
        data_hora=timestamp  
    )
    print(f"Salvo no banco: {sensor_nome} -> Estado: {estado}, Timestamp: {data_hora}")


# Verifica se o estado mudou e salva no banco
def verifica_sensor(sensor_nome, SENSOR_PIN, sensor_estado):
    if SENSOR_PIN.is_pressed and sensor_estado != 1:
        salvar_dados_no_banco(sensor_nome, 1)
        return 1  # Atualiza o estado

    if not SENSOR_PIN.is_pressed and sensor_estado != 0:
        salvar_dados_no_banco(sensor_nome, 0)
        return 0  # Atualiza o estado

    return sensor_estado  # Estado inalterado

# Loop principal
def coleta_dados():
    sensor_estado = {"Sensor_Silo_Superior": 3, "Sensor_Silo_Inferior": 3, 
                     "Sensor_Caixinha_Conectores": 3, "Sensor_Esteira": 3}

    while True:
        sensores = {
            "Sensor_Silo_Superior": MagicMock(),
            "Sensor_Silo_Inferior": MagicMock(),
            "Sensor_Caixinha_Conectores": MagicMock(),
            "Sensor_Esteira": MagicMock(),
        }

        for nome, pin in sensores.items():
            simula_sensor(pin, "HIGH" if sensor_estado[nome] == 0 else "LOW")
            sensor_estado[nome] = verifica_sensor(nome, pin, sensor_estado[nome])

        time.sleep(10)

