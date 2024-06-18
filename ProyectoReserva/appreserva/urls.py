from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'canchas', views.CanchaViewSet)
router.register(r'disponibilidad', views.DisponibilidadCanchaViewSet)
router.register(r'reservas', views.ReservaViewSet)
router.register(r'pagos', views.PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
