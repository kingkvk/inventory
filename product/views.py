from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.decorators import api_view

from .models import Users,Product,OrderDetails
from .serializers import UserSerializers,ProductSerializers,OrderDetailsSerializers

# Create your views here.

@api_view(['POST'])
def register_user(request):
    users=UserSerializers(data=request.data)
    print(users)
    if not  users.is_valid():
        return Response(data=user.errors,status=403)
    users.save()
    return Response({'message':'User Registered Successfully'})


@api_view(['POST'])
def create_product(request):
    product=ProductSerializers(data=request.data)
    if not product.is_valid():
        return Response(data=product.errors,status=403)
    product.save()
    return Response({'message':'Product Created Successfully'})

@api_view(['POST'])
def create_order(request):
    order_details=OrderDetailsSerializers(data=request.data)
    if not order_details.is_valid():
        return Response(data=order.errors,status=403)
    
    product_id=request.data['product_id']
    user_id=request.data['user_id']

    product_detail=Product.objects.get(pk=product_id)
    product_quantity=product_detail.product_quantity
    if product_quantity<=0:
        return Response({'message':'Product is out of stock'})
       
    order_details.save()
    product_data={
        'product_quantity':product_quantity-1
    }
    protduct_update=ProductSerializers(product_detail,data=product_data,partial=True)
    if not protduct_update.is_valid():
        return Response(data=protduct_update.errors,status=403)
    protduct_update.save()
    return Response({'message':'Order Created Successfully'})
    
    

@api_view(['GET'])
def user_list(request):
    users=Users.objects.all()
    serializer=UserSerializers(users,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_list(request):
    products=Product.objects.all()
    serializer=ProductSerializers(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_order_details(request, user_id):
    user_order_details=[]
    orders=list(OrderDetails.objects.filter(user_id=user_id).values('product_id'))

    for o in orders:
        orderdata=Product.objects.get(pk=o['product_id'])
        serializer=ProductSerializers(orderdata)
        user_order_details.append(serializer.data)
    return Response(user_order_details)
