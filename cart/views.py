from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CartDetails,CartSerializer
from rest_framework import status
from .models import Cart

@api_view(['POST'])
def create_cart(request):
    user=request.data.get('users')
    product=request.data.get('product')
    quantity=request.data.get('quantity')

    carts=Cart.objects.filter(
        users=user,
        product=product
        )
    
    if carts.exists():

        return Response({'message':'already exists'},status=status.HTTP_200_OK)
    
    Cart.objects.create(
        users_id=user,
        product_id =product,
        quantity=quantity
    )

    return Response({'message':"added to cart"},status=status.HTTP_201_CREATED)


@api_view(['GET'])
def fetch_cart(request):
    result = request.query_params.get('user_id')
    value=Cart.objects.all()
    c=len(value)
    if result:
        value = value.filter(users=result)
    serializer=CartDetails(value,many=True,context={'request':request})
    return Response({'count':c,'message':'data fetched successfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_cart(request,pk):
    table = Cart.objects.get(pk=pk)
    table.delete()
    return Response({'message':'data deleted successfully'},status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_cart(request, pk):

    action = request.data.get('action')

    value = Cart.objects.get(pk=pk)

    if action == "increase":
        value.quantity += 1

    elif action == "decrease":

        if value.quantity > 1:
            value.quantity -= 1

    value.save()

    serializer = CartSerializer(value)

    return Response(
        {
            'message':'updated successfully',
            'data':serializer.data
        },
        status=status.HTTP_200_OK
    )