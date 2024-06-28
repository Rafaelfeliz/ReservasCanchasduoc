from django.contrib import admin
from .models import Cliente, Cancha, DisponibilidadCancha, Reserva, Pago

admin.site.register(Cliente)
admin.site.register(Cancha)
admin.site.register(DisponibilidadCancha)
admin.site.register(Reserva)
admin.site.register(Pago)
