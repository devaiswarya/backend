from django.urls import path
from .views import create_cart,fetch_cart,delete_cart,update_cart

urlpatterns=[
    path('create',create_cart,name='create_cart'),
    path('fetch',fetch_cart,name='fetch_cart'),
    path('delete/<int:pk>',delete_cart,name='delete_cart'),
    path('update/<int:pk>',update_cart,name='update_cart')
]