from rest_framework.decorators import api_view
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import user

@api_view(['POST'])
def create_user(request):
    email=request.data.get('email')
    number =request.data.get('number')
    a=len(number)
    password = request.data.get('password')
    confirm = request.data.get('confirm')
    if user.objects.filter(email=email).exists():
        return Response({'message':'email is already exists'},status=status.HTTP_400_BAD_REQUEST)
    if a!=10:
        return Response({'message':'please enter the valid phone number'},status=status.HTTP_400_BAD_REQUEST)
    if user.objects.filter(number=number).exists():
        return Response({'message':'phone number already exists'},status=status.HTTP_400_BAD_REQUEST)
    if password != confirm:
        return Response({'message':'password does not match'},status=status.HTTP_400_BAD_REQUEST)
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response ({'message':'data created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    else:
        return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    email=request.data.get('email')
    password = request.data.get('password')
    if user.objects.filter(email=email).exists():
        value=user.objects.filter(email=email).first()  
        result = UserSerializer(value)
        if password == value.password:
            return Response ({'message':'login successfully','data':result.data},status=status.HTTP_200_OK)
        else :
            return Response ({'message':'password invalid'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response ({'message':'email does not exists'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request):
    value=user.objects.all()
    result=UserSerializer(value,many=True)
    return Response ({'message':'data fetched successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_data(request,pk):
    value=user.objects.get(pk=pk)
    result=UserSerializer(value)
    return Response({'message':'data fetched successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_user_data(request,pk):
    value=user.objects.get(pk=pk)
    serializer=UserSerializer(value,data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response({'message':'data updated successfully'},status=status.HTTP_202_ACCEPTED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request,pk):
    table=user.objects.get(pk=pk)
    table.delete()
    return Response({'message':'data deleted successfully'},status=status.HTTP_204_NO_CONTENT)
