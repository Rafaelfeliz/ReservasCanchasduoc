from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CanchaViewSet, DisponibilidadCanchaViewSet, ReservaViewSet, PagoViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('cancha', CanchaViewSet)
router.register('disponibilidadcancha', DisponibilidadCanchaViewSet)
router.register('reserva', ReservaViewSet)
router.register('pago', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
