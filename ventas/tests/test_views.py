from django import urls
from django.contrib.auth import get_user_model
import pytest


##Los tests al ejecutarlos dejan la colección "ventas_producto" sin registros.

# @pytest.mark.django_db
# class TestViews:
#     def test_render_views(self):
#         pass
