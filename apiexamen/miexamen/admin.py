from django.contrib import admin
from .models import Producto, Usuario, Listado, Tienda

admin.site.register( Producto )
admin.site.register( Usuario )
admin.site.register( Listado )
admin.site.register( Tienda )