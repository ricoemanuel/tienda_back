from django.urls import path, include
from rest_framework import routers
from .views import CarritoFilter, ItemsFilter, TiendaViewSet, ProductoViewSet, UsuariosViewSet, CarritoViewSet, ItemsViewSet, setItem

router = routers.DefaultRouter()

router.register(r"tiendas", TiendaViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"usuarios", UsuariosViewSet)
router.register(r"carritos", CarritoViewSet)
router.register(r"items", ItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("carritoFilter/", CarritoFilter.as_view()),
    path("ItemsFilter/", ItemsFilter.as_view()),
    path("setItem/", setItem.as_view()),
    
]
