from django.urls import path
from .views import create_fav,delete_fav,fetch_fav

urlpatterns=[
    path('create/',create_fav,name='create_fav'),
    path("fetched/",fetch_fav,name='fetch_fav'),
    path('delete/<int:pk>/',delete_fav,name='delete_fav'),
]