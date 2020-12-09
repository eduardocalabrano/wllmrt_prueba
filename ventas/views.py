from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from .models import Producto
from django.template.loader import render_to_string
from django.db.models import Q

def carga_inicial(request):
    items = Producto.objects.values('brand', 'image', 'description', 'price')
    return render(request, 'ventas/lista_productos.html', {'items': items})

def valida_palidromo(request):
    '''
    Se recibe la palabra a buscar como "producto" pero antes se valida si es un palidromo
    '''
    busqueda = request.GET.get('prod_buscar', None)
    inverso = busqueda[::-1]
    if(busqueda == inverso):
        respuesta='Y'
    else:
        respuesta='N'
    return HttpResponse(respuesta)


def productos_filtrados(request, cadena):
    pal = 'N'
    try:
      count_resultados_id = Producto.objects.filter(id=cadena).count()
    except:
      count_resultados_id = 0
    if(count_resultados_id > 0):
        resultado = Producto.objects.values('brand', 'image', 'description', 'price').filter(id=cadena)
    else:
        resultado = Producto.objects.values('brand', 'image', 'description', 'price').filter(Q(brand__contains=cadena)|Q(description__contains=cadena))
    if(len(cadena) >= 3 and (cadena == cadena[::-1])):
        pal = 'Y'
    return render(request, 'ventas/lista_productos.html', {'items': resultado, 'palidrome':pal})
