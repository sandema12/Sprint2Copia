from django.db import models

class Order(models.Model):
    status = models.CharField(max_length=50)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    amount = models.FloatField()
    method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
