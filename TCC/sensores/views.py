from sensores.models import Sensor,Logprevisaoia, Registrosinal, Previsaoia
from sensores.serializers import SensorSerializer, LogprevisaoiaSerializer, RegistrosinalSerializer, PrevisaoiaSerializer
from rest_framework import viewsets

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class LogprevisaoiaViewSet(viewsets.ModelViewSet):
    queryset = Logprevisaoia.objects.all()
    serializer_class = LogprevisaoiaSerializer

class RegistrosinalViewSet(viewsets.ModelViewSet):
    queryset = Registrosinal.objects.all()
    serializer_class = RegistrosinalSerializer

class PrevisaoiaViewSet(viewsets.ModelViewSet):
    queryset = Previsaoia.objects.all()
    serializer_class = PrevisaoiaSerializer

               
