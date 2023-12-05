from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=254)
    def __str__(self):
        return self.customer_name

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    def __str__(self):
        return self.restaurant_name

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=400)
    item_price = models.IntegerField(default=0)
    item_seller = models.PositiveIntegerField(default=1) # refers to the restaurant ID
    def __str__(self):
        return self.item_name

class Order(models.Model):
    order_customerId = models.IntegerField(default=0)
    order_restaurantId = models.IntegerField(default=0)
    order_status = models.SmallIntegerField(choices=((1, "received"), (2, "preparing"), (3, "ready"), (4, "delivered")), default=1)
    order_items = models.JSONField()
    '''def __str(self):
        return "{}".format(self.Order)'''

