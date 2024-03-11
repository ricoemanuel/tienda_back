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

class ModelFilter(APIView):
    def __init__(self, model, serializer):
        super().__init__()
        self.model = model
        self.serializer = serializer

    def post(self, request):
        filter_data = request.data
        query_set = self.model.objects.filter(**filter_data)
        res = [self.serializer(item).data for item in query_set]
        return Response(res)

class CarritoFilter(ModelFilter):
    def __init__(self):
        super().__init__(Carrito, CarritoSerializer)

class ItemsFilter(ModelFilter):
    def __init__(self):
        super().__init__(Items, ItemsSerializer)
