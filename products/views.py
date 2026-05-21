from rest_framework.decorators import api_view
from .serializer import ProductSerializer,ProductDetails
from rest_framework.response import Response
from rest_framework import status
from .models import Product


@api_view(['POST'])
def create_product(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    else:
        return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_product(request):
    category=request.query_params.get('cat_id')
    sort=request.query_params.get('sort')
    find = request.query_params.get('find')

    value=Product.objects.all()
    if category:
        value=value.filter(category=category)

    if sort == 'low':
         value=  value.order_by('product_price')

    # High to Low
    elif sort == 'high':
         value =  value.order_by('-product_price')

    if find :
        value = value.filter(product_name__icontains=find)

    limit = request.query_params.get('limit')
    offset = request.query_params.get('offset')

    # paginate only if params passed
    if limit not in [None, ''] and offset not in [None, '']:

        limit = int(limit)
        offset = int(offset)

        start = offset * limit
        end = start + limit

        data = value[start:end]

        serializer = ProductSerializer(
            data,
            many=True,
            context={'request': request}
        )

        return Response({
            'total': value.count(),
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    
    result = ProductSerializer(value,many=True,context={'request':request})
    return Response({'message':'data fetched successfully','data':result.data},status=status.HTTP_200_OK)


@api_view(['GET'])
def get_pro(request,pk):
    table = Product.objects.get(pk=pk)
    result=ProductDetails (table,context={'request':request})
    return Response({'message':'data fetched successfully','data':result.data},status=status.HTTP_200_OK)


@api_view(['PUT']) 
def update_product(request,pk):
    value=Product.objects.get(pk=pk)
    serializer=ProductSerializer(value,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data updated successfully','data':serializer.data},status=status.HTTP_200_OK)
    else:
         return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['delete'])
def delete_product(request,pk):
    table=Product.objects.get(pk=pk)
    table.delete()
    return Response({'message':'data deleted successfully'},status=status.HTTP_204_NO_CONTENT)


