from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CanchaViewSet, DisponibilidadCanchaViewSet, ReservaViewSet, PagoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'canchas', CanchaViewSet)
router.register(r'disponibilidad-canchas', DisponibilidadCanchaViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
