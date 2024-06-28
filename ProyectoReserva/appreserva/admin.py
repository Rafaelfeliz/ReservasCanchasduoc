from django.contrib import admin
from .models import Cancha, DisponibilidadCancha, Reserva, Pago

admin.site.register(Cancha)
admin.site.register(DisponibilidadCancha)
admin.site.register(Reserva)
admin.site.register(Pago)
