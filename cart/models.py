from django.db import models
from user.models import user
from products.models import Product

# Create your models here.
class Cart(models.Model):
    users=models.ForeignKey(user,on_delete=models.CASCADE,related_name="cart")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cart")
    quantity=models.IntegerField()

    def __str__(self):
        return 'Cart'