from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.DecimalField()
    category = models.TextField()
    description = models.TextField()