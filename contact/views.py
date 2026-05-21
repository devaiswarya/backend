from django.shortcuts import render
from rest_framework.response import Response
from .models import Contact
from rest_framework.decorators import api_view
from .serializer import ContactSerializer
from rest_framework import status
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random


@api_view(['POST'])
def mailSend(request):
    email=request.data.get('email')
    name=request.data.get('name')
    otp=''
    for i in range(6):
        digit=random.randint(0,9) 
        otp+=str(digit)

    serializer=ContactSerializer(data=request.data)
    if serializer.is_valid():
        subject="Welcome to Alo Infotech – You're In!"
        message=f"Hi {name},Thanks for subscribing to Alo Infotech news_letter!{otp}"
        recipient_list=[email]
        send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently=True)
        serializer.save()
        return Response({'message': 'Contact created', 'Contact': serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

