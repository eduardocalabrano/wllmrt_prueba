from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Producto
from django.db.models import Q

def carga_inicial(request):
    # Se muestran todos los productos en una primera carga
    items = Producto.objects.values('brand', 'image', 'description', 'price').order_by('id')
    p = Paginator(items, 15)
    page1 = p.page(1)
    total_paginas = p.num_pages
    next_page = 0
    if(total_paginas > 1):
        next_page = page1.next_page_number()
    return render(request, 'ventas/lista_productos.html', {'items': page1.object_list, 'num_paginas': total_paginas, 'sgte_pagina': next_page})

def productos_por_pagina(request, pagina):
    #vista que entrega el listado de productos sin filtro según el número de página solicitado
    next_page = 0
    prev_page = 1
    items = Producto.objects.values('brand', 'image', 'description', 'price').order_by('id')
    p = Paginator(items, 15)
    total_paginas = p.num_pages
    pagina_solicitada = p.page(pagina)
    if(pagina_solicitada.has_next()):
        next_page = pagina_solicitada.next_page_number()
    if(pagina_solicitada.has_previous()):
        prev_page = pagina_solicitada.previous_page_number()
    return render(request, 'ventas/lista_productos.html', {'items': pagina_solicitada.object_list, 'num_paginas': total_paginas, 'sgte_pagina': next_page, 'ant_pagina':prev_page})

def productos_filtrados(request, cadena):
    # Se recibe la cadena de búsqueda previa validación del JS
    pal = 'N'
    try:
        # En caso de ser posible el siguiente queryset, la cadena de búsqueda es un ID
      count_resultados_id = Producto.objects.filter(id=cadena).count()
    except:
      count_resultados_id = 0
    if(count_resultados_id > 0):
        # En caso de que la cadena es un ID, se realiza la búsqueda única
        resultado = Producto.objects.values('brand', 'image', 'description', 'price').filter(id=cadena)[:1]
    else:
        # En caso de que la cadena no sea un ID, se realiza la búsqueda en brand y description sin limite de productos
        resultado = Producto.objects.values('brand', 'image', 'description', 'price').filter(Q(brand__icontains=cadena)|Q(description__icontains=cadena))
    if(len(cadena) >= 3 and (cadena == cadena[::-1])):
        # Se evalua el largo de la cadena (min. 3) y que esta sea un palindrome.
        pal = 'Y'
    # Se vuelve a llamar al template enviando los productos encontrados y si la cadena es palindrome
    return render(request, 'ventas/lista_productos.html', {'items': resultado, 'palindrome':pal})
