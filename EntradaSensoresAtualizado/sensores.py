import json

class Sensores:
    def __init__(self, nome_sensor, sinal_sensor, data_da_deteccao, hora_da_deteccao):
        self._nome_sensor = nome_sensor
        self._sinal_sensor = sinal_sensor
        self._data_da_deteccao = data_da_deteccao
        self._hora_da_deteccao = hora_da_deteccao


    def __str__(self):
        return f'Nome Do Sensor : {self._nome_sensor}\nSinal Detectado: {self._sinal_sensor}\nData Da detecção: {self._data_da_deteccao}\nHora Da Detecção: {self._hora_da_deteccao}'
    

    # Função que retorna dicionario feito com base nos atributos da classe convertidos em Json
    def transforma_dicionario_json(self):
        dicionario_informacoes_sensores = self.__dict__
        json_sensor = json.dumps(dicionario_informacoes_sensores, indent=4)
       
        return json_sensor