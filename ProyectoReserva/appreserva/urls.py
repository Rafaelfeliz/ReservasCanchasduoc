from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'canchas', views.CanchaViewSet)
router.register(r'disponibilidades', views.DisponibilidadCanchaViewSet)
router.register(r'pagos', views.PagoViewSet)
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
