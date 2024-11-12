from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from blogs.models import House, Order
from blogs.serializers import HouseDetailSerializer, OrderSerializer, HouseListSerializer, OrderListSerializer, \
    HouseUpdateSerializer, HouseCreateSerializer, OrderDetailSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def house_list_view(request):
    houses = House.objects.all()
    serializer = HouseListSerializer(houses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def house_detail_view(request, pk):
    try:
        house = House.objects.get(id=pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HouseDetailSerializer(house)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        order_data = {
            'house': house.id,
            'buyer': request.user.id,
            'phone_number': request.data.get('phone_number')
        }
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order = order_serializer.save(house=house, buyer=request.user)
            response_data = {
                'order': OrderSerializer(order).data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


@api_view(['GET'])
@permission_classes([IsStaffUser])
def staff_house_list_view(request):
    houses = House.objects.all()
    serializer = HouseListSerializer(houses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsStaffUser])
def staff_house_detail_view(request, pk):
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return Response({'message': 'House is not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = HouseDetailSerializer(house)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsStaffUser])
def house_create_view(request):
    serializer = HouseCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsStaffUser])
def house_update_view(request, pk):
    house = get_object_or_404(House, pk=pk)
    partial = request.method == 'PATCH'
    serializer = HouseUpdateSerializer(instance=house, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsStaffUser])
def house_delete_view(request, pk):
    house = get_object_or_404(House, pk=pk)
    house.delete()
    return Response({"detail": "House successfully deleted."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsStaffUser])
def order_list_view(request):
    orders = Order.objects.all()
    serializer = OrderListSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsStaffUser])
def order_detail_view(request, pk):
    try:
        order = get_object_or_404(Order, pk=pk)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderDetailSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsStaffUser])
def order_delete_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return Response({"detail": "Order successfully deleted."}, status=status.HTTP_204_NO_CONTENT)