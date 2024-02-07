from django.db import models
from django.utils.html import mark_safe

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="55" height="55" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.name
    
class Video(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/')

    def __str__(self) -> str:
        return self.title  