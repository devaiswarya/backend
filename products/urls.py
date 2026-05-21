from django.urls import path
from .views import create_product,update_product,delete_product,get_pro,get_product

urlpatterns=[
    path('create',create_product,name='create_product'),
    path('fetched',get_product,name='get_product'),
    path('retrieve/<int:pk>',get_pro,name='get_pro'),
    path('update/<int:pk>',update_product,name='update_product'),
    path('delete/<int:pk>',delete_product,name='delete_product'),
]