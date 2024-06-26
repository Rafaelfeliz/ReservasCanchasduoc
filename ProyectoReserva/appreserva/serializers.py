from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Cancha, DisponibilidadCancha, Reserva, Pago

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = '__all__'

class DisponibilidadCanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisponibilidadCancha
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
