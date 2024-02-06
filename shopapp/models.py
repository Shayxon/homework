from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.name
    
class Video(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/')

    def __str__(self) -> str:
        return self.title  