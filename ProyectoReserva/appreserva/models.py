from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.usuario}, {self.contraseña}, {self.carrera}, {self.email}"


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)  # Ejemplo: Futbol, Basquetbol, etc.

    def __str__(self):
        return self.nombre

class DisponibilidadCancha(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.cancha.nombre} - {self.fecha} {self.hora_inicio}-{self.hora_fin}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.cliente.user.username} - {self.cancha.nombre} - {self.fecha_reserva} {self.hora_inicio}-{self.hora_fin}"

class Pago(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)  # Ejemplo: Tarjeta, Efectivo, etc.

    def __str__(self):
        return f"Pago de {self.reserva.cliente.user.username} - {self.monto}"
