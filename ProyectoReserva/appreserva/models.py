from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=50) 
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre, self.usuario, self.contraseña, self.carrera, self.email
    def __str__(self):
        user: User = self.user  # Sugerencia de tipo
        return user.username

class Cancha(models.Model):
    numero = models.IntegerField() # 1, 2, 3, 4, 5, 6.
    tipo = models.CharField(max_length=50) #pasto sintetico, pasto natural, cemento
    precio = models.IntegerField() # 30.000 , algun descuento por primer vez, a 15.000
    def __str__(self):
        return self.numero, self.tipo, self.precio 

class DisponibilidadCancha(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    dia_semana = models.DateField()       # 1=Lunes, 2=Martes, ..., 7=Domingo
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    reservado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cancha.numero} - {self.dia_semana} {self.hora_inicio}-{self.hora_fin}"

class Reserva(models.Model): #Resumen de la reserva
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    disponibilidad = models.ForeignKey(DisponibilidadCancha, on_delete=models.CASCADE)
    pagado = models.BooleanField()
    pago = models.OneToOneField(Pago, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return f"{self.cliente} - {self.disponibilidad} - {self.pagado} - {self.pago}"

class Pago(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    hora_pago = models.TimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)  # Ejemplo: Tarjeta; debito, credito, transferencia, etc.

    def __str__(self):
        return f"Pago de {self.reserva.cliente} - {self.monto}, {self.fecha_pago} {self.hora_pago} {self.metodo_pago}"
