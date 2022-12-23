from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    in_stock = models.BooleanField(default=True)
    image = models.URLField()

    def __str__(self) -> str:
        return self.name
