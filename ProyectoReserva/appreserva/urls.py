from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import userViewSet, CanchaViewSet, DisponibilidadCanchaViewSet, ReservaViewSet, PagoViewSet, ClienteViewSet


router = DefaultRouter()
router.register('cliente', ClienteViewSet)
router.register('user', userViewSet)
router.register('cancha', CanchaViewSet)
router.register('disponibilidadcancha', DisponibilidadCanchaViewSet)
router.register('reserva', ReservaViewSet)
router.register('pago', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
