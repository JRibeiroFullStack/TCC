from datetime import datetime
import time
import json, os
from sensores import Sensores
from unittest.mock import MagicMock

sensores_dados = {}


# Função para formatar a hora atual
def formatacao_de_coleta():
    hora_atual = datetime.now().strftime("%H:%M:%S")
    data_atual = datetime.now().strftime("%d/%m/%Y")

    return hora_atual, data_atual


# Função para ser retirada após a instalçao fisica dos sensores e suas configurações de entrada na rasp
# Função para simular a ativação de um sensor
def simula_sensor(SENSOR_PIN, estado):
    if estado == "HIGH":
        SENSOR_PIN.is_pressed = True  
    else:
        SENSOR_PIN.is_pressed = False 


# Função de verificação, caso o arquivo ja exista
def verificacao_json():
    

    #Verifica se ja existe o Json para não criar outro
    if not os.path.exists('sensores_data.json'):
        with open('sensores_data.json', 'w') as arquivo_json:
            json.dump(sensores_dados, arquivo_json, indent=4)

    # Carrega os dados existentes do arquivo JSON
    try:
        with open('sensores_data.json', 'r') as arquivo_json:
            sensores_dados = json.load(arquivo_json)
    except json.JSONDecodeError:
        pass


# Estamos agrupando em listas pode nome de sensores. Independente de sinal de entrada.
# Função verifica se ja existe a lista do sensor, buscando a referencia pelo nome.
def verificaca_nome_sensor_lista(sensor,sensor_nome, sensores_dados):
    if sensor_nome in sensores_dados:
        sensores_dados[sensor_nome].append(sensor.transforma_dicionario_json())
    else:
        sensores_dados[sensor_nome] = [sensor.transforma_dicionario_json()]
        
    # Escreve o dicionário atualizado no arquivo JSON
    with open('sensores_data.json', 'w') as arquivo_json:
        json.dump(sensores_dados, arquivo_json, indent=4)


#Fução de criação do objeto e transformação do Json
def verifica_sensor(sensor_nome, SENSOR_PIN, sensor_estado):
    verificacao_json()
    if SENSOR_PIN.is_pressed and sensor_estado != 1:
        data, hora = formatacao_de_coleta()
        sensor = Sensores(sensor_nome, 1, data, hora)
        print(sensor.transforma_dicionario_json())
        sensor_estado = 1
        verificaca_nome_sensor_lista(sensor, sensor_nome, sensores_dados)
        return sensor, sensor_estado

    if not SENSOR_PIN.is_pressed and sensor_estado != 0:
        data, hora = formatacao_de_coleta()
        sensor = Sensores(sensor_nome, 0, data, hora)
        print(sensor.transforma_dicionario_json())
        sensor_estado = 0
        verificaca_nome_sensor_lista(sensor, sensor_nome, sensores_dados)
        return sensor, sensor_estado
    
    return None, sensor_estado


# Função principal
def saida():
    sensor_estado_1 = 3
    sensor_estado_2 = 3
    sensor_estado_3 = 3
    sensor_estado_4 = 3

    while True:

        # Só entra em cada sinal após ser alterado na função
        # Sensor Silo Superior (com estado alternado entre HIGH e LOW)
        SENSOR_1_PIN = MagicMock()  # Sensor Silo Superior
        if sensor_estado_1 == 1:
            simula_sensor(SENSOR_1_PIN, "LOW")
        else:
            simula_sensor(SENSOR_1_PIN, "HIGH")
        _, sensor_estado_1 = verifica_sensor('Sensor_Silo_Superior', SENSOR_1_PIN, sensor_estado_1)



        # Só entra em cada sinal após ser alterado na função
        # Sensor Silo Inferior (com estado alternado entre HIGH e LOW)
        SENSOR_2_PIN = MagicMock()  # Sensor Silo Inferior
        if sensor_estado_2 == 1:
            simula_sensor(SENSOR_2_PIN, "LOW")
        else:
            simula_sensor(SENSOR_2_PIN, "HIGH")
        _, sensor_estado_2 = verifica_sensor('Sensor_Silo_inferior', SENSOR_2_PIN, sensor_estado_2)




        # Só entra em cada sinal após ser alterado na função
        # Sensor Caixinha de Conectores (com estado alternado entre HIGH e LOW)
        SENSOR_3_PIN = MagicMock()  # Sensor Caixinha de Conectores
        if sensor_estado_3 == 1:
            simula_sensor(SENSOR_3_PIN, "LOW")
        else:
            simula_sensor(SENSOR_3_PIN, "HIGH")
        _, sensor_estado_3 = verifica_sensor('Sensor_Caixinha_Conectores', SENSOR_3_PIN, sensor_estado_3)



        # Só entra em cada sinal após ser alterado na função
        # Sensor Esteira (com estado alternado entre HIGH e LOW)
        SENSOR_4_PIN = MagicMock()
        if sensor_estado_4 == 1:
            simula_sensor(SENSOR_4_PIN, "LOW")
        else:
            simula_sensor(SENSOR_4_PIN, "HIGH")
        _, sensor_estado_4 = verifica_sensor('Sensor_Esteira', SENSOR_4_PIN, sensor_estado_4)
        
        time.sleep(10)


# Função para ler campos especificos de um sensor especifico
def leitura_json(sensor_nome, campo_desejado):
    caminho_arquivo = 'sensores_data.json'

    # Abrir o arquivo e carregar o conteúdo JSON
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)

    dados_sensor_especifico = dados[sensor_nome]

    for registro in dados_sensor_especifico:
        registros_campo = json.loads(registro)
        print( f"{sensor_nome}: {registros_campo[campo_desejado]}")


