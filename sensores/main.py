from unittest.mock import MagicMock
import time
from datetime import datetime
from sensores import Sensores
import json

# Função para formatar a hora atual
def formata_hora():
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    return hora_formatada

# Função para formatar a data atual
def formata_data():
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y")
    return data_formatada


# Função para ser retirada após a instalçao fisica dos sensores e suas configurações de entrada na rasp
# Função para simular a ativação de um sensor
def simula_sensor(SENSOR_PIN, estado):
    if estado == "HIGH":
        SENSOR_PIN.is_pressed = True  
    else:
        SENSOR_PIN.is_pressed = False 




# Função genérica para verificar sensores
def verfica_sensor(sensor_nome, SENSOR_PIN, sensor_estado):
    if SENSOR_PIN.is_pressed and sensor_estado != 1:
        with open('sensores_data.json', 'a') as arquivo_json:
            sensor = Sensores(sensor_nome, 1, formata_data(), formata_hora())
            print(sensor.transforma_dicionario_json())
            sensor_estado = 1  # Atualiza o estado do sensor para 1
            arquivo_json.write(sensor.transforma_dicionario_json() + "\n") # Escreve no arquivo Json
            return sensor, sensor_estado

    if not SENSOR_PIN.is_pressed and sensor_estado != 0:
        with open('sensores_data.json', 'a') as arquivo_json:
            sensor = Sensores(sensor_nome, 0, formata_data(), formata_hora())
            print(sensor.transforma_dicionario_json())
            sensor_estado = 0  
            arquivo_json.write(sensor.transforma_dicionario_json() + "\n") # Escreve no arquivo Json
            return sensor, sensor_estado

    return None, sensor_estado  




def main():
    sensor_estado_1 = 3
    sensor_estado_2 = 3
    sensor_estado_3 = 3


    while True:

        # Só entra em cada sinal após ser alterado na função
        # Sensor Silo Superior (com estado alternado entre HIGH e LOW)
        SENSOR_1_PIN = MagicMock()  # Sensor Silo Superior
        if sensor_estado_1 == 1:
            simula_sensor(SENSOR_1_PIN, "LOW")
        else:
            simula_sensor(SENSOR_1_PIN, "HIGH")
        _, sensor_estado_1 = verfica_sensor('Sensor_Silo_Superior', SENSOR_1_PIN, sensor_estado_1)



        # Só entra em cada sinal após ser alterado na função
        # Sensor Silo Inferior (com estado alternado entre HIGH e LOW)
        SENSOR_2_PIN = MagicMock()  # Sensor Silo Inferior
        if sensor_estado_2 == 1:
            simula_sensor(SENSOR_2_PIN, "LOW")
        else:
            simula_sensor(SENSOR_2_PIN, "HIGH")
        _, sensor_estado_2 = verfica_sensor('Sensor_Silo_inferior', SENSOR_2_PIN, sensor_estado_2)




        # Só entra em cada sinal após ser alterado na função
        # Sensor Caixinha de Conectores (com estado alternado entre HIGH e LOW)
        SENSOR_3_PIN = MagicMock()  # Sensor Caixinha de Conectores
        if sensor_estado_3 == 1:
            simula_sensor(SENSOR_3_PIN, "LOW")
        else:
            simula_sensor(SENSOR_3_PIN, "HIGH")
        _, sensor_estado_3 = verfica_sensor('Sensor_Caixinha_Conectores', SENSOR_3_PIN, sensor_estado_3)

        
        time.sleep(10)

if __name__ == '__main__':
    main()
