from django.urls import reverse, resolve
# import pytest

class TestUrls:
    def test_url_inicial(self):
        path = reverse('carga_inicial')
        assert resolve(path).view_name == 'carga_inicial'
