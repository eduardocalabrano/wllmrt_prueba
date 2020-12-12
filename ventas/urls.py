from django.urls import path
from . import views

urlpatterns = [
    path('', views.carga_inicial, name='carga_inicial'),
    path('filtro/<cadena>', views.productos_filtrados, name='filtro_productos'),
    path('all/<pagina>', views.productos_por_pagina, name='productos_por_pagina'),
]
