from django.shortcuts import render
from .models import Producto

def carga_inicial(request):
    items = Producto.objects.values('brand', 'image', 'description', 'price')
    return render(request, 'ventas/pantalla_inicial.html', {'items': items})
