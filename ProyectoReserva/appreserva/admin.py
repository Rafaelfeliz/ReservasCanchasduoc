from django.contrib import admin
from .models import Cancha, DisponibilidadCancha, Reserva, Pago

# Registrar los demás modelos en el admin de Django
admin.site.register(Cancha)
admin.site.register(DisponibilidadCancha)
admin.site.register(Reserva)
admin.site.register(Pago)

