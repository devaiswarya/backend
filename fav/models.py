from django.db import models
from user.models import user
from products.models import Product

# Create your models here.
class fav(models.Model):
    users = models.ForeignKey(user,on_delete=models.CASCADE,related_name='fav')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='fav')

    def __str__(self):
        return 'fav'
