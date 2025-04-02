import threading
from sensores.sensor_utils import coleta_dados

def start_coleta_dados():
    thread = threading.Thread(target = coleta_dados)
    thread.deamon =  True
    thread.start()