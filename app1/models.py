from django.db import models

# Create your models here.

class AddProductModel(models.Model):
    brand = models.CharField(max_length = 50)
    name = models.CharField(max_length = 30)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}: {self.price}"
    
