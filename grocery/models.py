from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} | {self.market.name}'


class Grocery(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name
