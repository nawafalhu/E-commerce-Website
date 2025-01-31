from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Purchase', related_name='products')

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} purchased {self.product.name}'