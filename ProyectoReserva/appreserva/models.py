from django.db import models  # type: ignore
from django.contrib.auth.models import User

class Cancha(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    numero_cancha = models.IntegerField()

    def __str__(self):
        return f"Cancha {self.numero_cancha} - {self.fecha} {self.hora}"

class DisponibilidadCancha(models.Model):
    numero_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Cancha {self.numero_cancha.numero_cancha} - {self.fecha} {self.hora}"

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - Cancha {self.numero_cancha.numero_cancha} - {self.fecha} {self.hora}"

class Pago(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago de {self.reserva} - {self.monto}"
