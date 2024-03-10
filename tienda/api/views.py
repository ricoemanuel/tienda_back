from rest_framework import viewsets
from tienda.models import Tienda, Producto, Usuarios, Carrito, Items
from .serializers import TiendaSerializer, ProductoSerializer, UsuariosSerializer, CarritoSerializer, ItemsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class CarritoFilter(APIView):
    def post(self, request):
        carrito_filter=request.data
        carritos=Carrito.objects.filter(**carrito_filter)
        res=[]
        for carrito in carritos:
            res.append(CarritoSerializer(carrito).data)
        return Response(res)
