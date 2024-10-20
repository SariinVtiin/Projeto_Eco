from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TotemViewSet, ColetaViewSet, UsuarioViewSet, RotaViewSet

router = DefaultRouter()
router.register(r'totens', TotemViewSet)
router.register(r'coletas', ColetaViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'rota', RotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
