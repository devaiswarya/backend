from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import FavSerializer,FavProduct
from rest_framework import status
from .models import fav


@api_view(['POST'])
def create_fav(request):
    value = request.data.get('product')
    if fav.objects.filter(product=value).exists():
        return Response({'message':'product already exists'},status=status.HTTP_400_BAD_REQUEST)
    serializer=FavSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"data created successfully","data":serializer.data},status=status.HTTP_201_CREATED)
    return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_fav(request):
    result = request.query_params.get('user_id')
    value = fav.objects.all()
    c=len(value)
    if result :
        value = value.filter(users=result)
    serializer=FavProduct(value,many=True,context={'request':request})
    return Response({'count':c,'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_fav(request,pk):
    table=fav.objects.get(pk=pk)
    table.delete()
    return Response({'message':'data deleted successfully'},status=status.HTTP_204_NO_CONTENT)

