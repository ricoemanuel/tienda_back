from django.urls import path, include
from rest_framework import routers
from .views import CarritoFilter, TiendaViewSet, ProductoViewSet, UsuariosViewSet, CarritoViewSet, ItemsViewSet

router = routers.DefaultRouter()

router.register(r"tiendas", TiendaViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"usuarios", UsuariosViewSet)
router.register(r"carritos", CarritoViewSet)
router.register(r"items", ItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("carritoFilter/", CarritoFilter.as_view()),
]
