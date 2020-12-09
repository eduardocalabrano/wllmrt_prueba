from django.urls import path
from . import views

urlpatterns = [
    path('', views.carga_inicial, name='carga_inicial'),
    path('ajax/valida_palidromo/', views.valida_palidromo, name='valida_palidromo'),
    path('filtro/<cadena>', views.productos_filtrados, name='filtro_productos'),
]
