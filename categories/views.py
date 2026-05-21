from rest_framework.decorators import api_view
from .serializer import CategoriesSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Category

@api_view(['POST'])
def create_categories(request):
    serializer=CategoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    else:
        return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_categories(request):
     value=Category.objects.all()
     result = CategoriesSerializer(value,many=True)
     return Response({'message':'data fetched successfully','data':result.data},status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cate(request,pk):
    value=Category.objects.get(pk=pk)
    result=CategoriesSerializer(value)
    return Response({'message':'data fetched successfully','data':result.data},status=status.HTTP_200_OK)
       

@api_view(['PUT'])
def update_categories(request,pk):
    value=Category.objects.get(pk=pk)
    serializer=CategoriesSerializer(value,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)
    else:
        return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['delete'])
def delete_categories(request,pk):
    value=Category.objects.get(pk=pk)
    value.delete()
    return Response({'message':'data deleted successfully'},status=status.HTTP_204_NO_CONTENT)