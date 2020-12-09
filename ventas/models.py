# from django.db import models
from djongo import models

class Producto(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    brand = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField()

    def __str__(self):
        return self.brand
