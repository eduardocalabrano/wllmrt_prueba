from mixer.backend.django import mixer
import pytest

##Los tests al ejecutarlos dejan la colección "ventas_producto" sin registros.

# @pytest.mark.django_db
# class TestModels:
#     def test_producto_tiene_precio(self):
#         producto = mixer.blend('ventas.Producto', price = 100)
#         assert producto.tiene_precio == True
#
#     def test_producto_no_tiene_precio(self):
#         producto = mixer.blend('ventas.Producto', price = 0)
#         assert producto.tiene_precio == False
