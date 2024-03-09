from django.contrib import admin

from tienda.models import Tienda,Producto, Carrito,Items, Usuarios


admin.site.register(Tienda)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Items)
admin.site.register(Usuarios)