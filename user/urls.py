from django.urls import path
from .views import create_user,get_user,get_user_data,update_user_data,delete_user,login_user

urlpatterns=[
    path("created",create_user,name="create_user"),
    path("fetched/",get_user,name="get_user"),
    path("getdata/<int:pk>",get_user_data,name="get_user_data"),
    path("update/<int:pk>",update_user_data,name="update_user_data"),
    path("delete/<int:pk>",delete_user,name="delete_user"),
    path('loginuser',login_user,name='login_user')
]