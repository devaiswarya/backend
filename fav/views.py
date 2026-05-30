from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import FavSerializer,FavProduct
from rest_framework import status
from .models import fav


@api_view(['POST'])
def create_fav(request):
 
    user = request.data.get('users')
    product = request.data.get('product')

    favs = fav.objects.filter(
        users=user,
        product=product
    )
    # REMOVE FAVOURITE
    if favs.exists():

        favs.delete()

        return Response({
            'message':'removed from favourite'
        },status=status.HTTP_200_OK)
    # ADD FAVOURITE
    fav.objects.create(
        users_id=user,
        product_id=product
    )
    return Response({
        'message':'added to favourite'
    },status=status.HTTP_201_CREATED)

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

