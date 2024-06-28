from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Cliente, Cancha, DisponibilidadCancha, Reserva, Pago
from.serializers import CanchaSerializer, DisponibilidadCanchaSerializer, ReservaSerializer, PagoSerializer, UserSerializer, ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
class DisponibilidadCanchaViewSet(viewsets.ModelViewSet):
    queryset = DisponibilidadCancha.objects.all()
    serializer_class = DisponibilidadCanchaSerializer

