from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Orders
from .serializers import OrderSerializer

# Create your views here.

# all orders
@api_view(["GET"])
def allOrders(request):
    orders=Orders.objects.all()
    order_serialize=OrderSerializer(orders,many=True)
    return Response(order_serialize.data)

# person orders
@api_view(['GET'])
def personOrders(request,number):
    orders=Orders.objects.filter(phoneOfCostumer=number)
    order_serialize=OrderSerializer(orders,many=True)
    return Response(order_serialize.data)

# saving all orders it gets json array
@api_view(["POST"])
def saveOrders(request):
    for i in range(len(request.data)):
        order=OrderSerializer(data=request.data[i])
        if order.is_valid():
            order.save()
    return Response("done")