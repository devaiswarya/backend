from django.db import models
from categories.models import Category

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    product_offer=models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity=models.IntegerField()
    des=models.TextField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
