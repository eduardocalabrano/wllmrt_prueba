from django.urls import path
from . import views

urlpatterns = [
    path('', views.carga_inicial, name='carga_inicial'),
]
