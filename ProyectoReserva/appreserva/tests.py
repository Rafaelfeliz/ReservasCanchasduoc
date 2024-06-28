from django.test import TestCase  # type: ignore
from django.contrib.auth.models import User
from .models import Cancha, DisponibilidadCancha, Reserva, Pago

class ModelsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()

        self.cancha = Cancha.objects.create(fecha="2023-01-01", hora="10:00:00", numero_cancha=1)
        self.disponibilidad = DisponibilidadCancha.objects.create(numero_cancha=self.cancha, fecha="2023-01-01", hora="10:00:00")
        self.reserva = Reserva.objects.create(user=self.user, numero_cancha=self.cancha, fecha="2023-01-01", hora="10:00:00")
        self.pago = Pago.objects.create(reserva=self.reserva, monto=1000.00, metodo_pago="Tarjeta")

    def test_cancha_creation(self):
        self.assertEqual(self.cancha.fecha.strftime("%Y-%m-%d"), "2023-01-01")
        self.assertEqual(self.cancha.numero_cancha, 1)

    def test_disponibilidad_creation(self):
        self.assertEqual(self.disponibilidad.fecha.strftime("%Y-%m-%d"), "2023-01-01")
        self.assertEqual(self.disponibilidad.hora.strftime("%H:%M:%S"), "10:00:00")

    def test_reserva_creation(self):
        self.assertEqual(self.reserva.fecha.strftime("%Y-%m-%d"), "2023-01-01")
        self.assertEqual(self.reserva.hora.strftime("%H:%M:%S"), "10:00:00")

    def test_pago_creation(self):
        self.assertEqual(self.pago.monto, 1000.00)
        self.assertEqual(self.pago.metodo_pago, "Tarjeta")
