from django.db import models


class Product(models.Model):
    manufactured = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    weigth = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
