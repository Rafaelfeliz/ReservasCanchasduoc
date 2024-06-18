from rest_framework import viewsets
from .models import Cliente, Cancha, DisponibilidadCancha, Reserva, Pago
from .serializers import ClienteSerializer, CanchaSerializer, DisponibilidadCanchaSerializer, ReservaSerializer, PagoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer

class DisponibilidadCanchaViewSet(viewsets.ModelViewSet):
    queryset = DisponibilidadCancha.objects.all()
    serializer_class = DisponibilidadCanchaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
