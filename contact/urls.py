from rest_framework.urls import path
from .views import mailSend

urlpatterns=[
    path('create',mailSend,name='mailSend'),
]