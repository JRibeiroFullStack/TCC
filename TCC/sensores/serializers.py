from rest_framework import serializers
from .models import Sensor,Logprevisaoia, Registrosinal, Previsaoia



#fields define quais campos vão ser expostos (Testando com todos)
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class LogprevisaoiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logprevisaoia
        fields = '__all__'

class RegistrosinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrosinal
        fields = '__all__'

class PrevisaoiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Previsaoia
        fields = '__all__'

