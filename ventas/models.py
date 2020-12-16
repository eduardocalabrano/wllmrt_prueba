from djongo import models

class Producto(models.Model):
    # Se utiliza mismos campos presentes en la base de datos Mongo
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    brand = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField()

    @property
    def tiene_precio(self):
        return self.price > 0

    def __str__(self):
        return self.brand
