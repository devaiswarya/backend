from django.urls import path
from .views import create_categories,get_cate,get_categories,update_categories,delete_categories

urlpatterns=[
    path('create',create_categories,name='create_categories'),
    path('fetched',get_categories,name='get_categories'),
    path('retrive/<int:pk>',get_cate,name='get_cate'),
    path('update/<int:pk>',update_categories,name='update_categories'),
    path('delete/<int:pk>',delete_categories,name='delete_categories')
]