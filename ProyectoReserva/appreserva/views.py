from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, CanchaSerializer, DisponibilidadCanchaSerializer, ReservaSerializer, PagoSerializer
from .models import Cancha, DisponibilidadCancha, Reserva, Pago

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer

class DisponibilidadCanchaViewSet(viewsets.ModelViewSet):
    queryset = DisponibilidadCancha.objects.all()
    serializer_class = DisponibilidadCanchaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
