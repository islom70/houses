from rest_framework import serializers

from accounts.serializers import SignUpSerializer
from .models import House, Order


class HouseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['title', 'location', 'image', 'is_sold']


class HouseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'title', 'description', 'price', 'location', 'area', 'bedrooms', 'bathrooms', 'image', 'is_sold']


class HouseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['title', 'description', 'price', 'location', 'area', 'bedrooms', 'bathrooms', 'image']


class HouseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['title', 'description', 'price', 'location', 'area', 'bedrooms', 'bathrooms', 'image', 'is_sold']


class OrderSerializer(serializers.ModelSerializer):
    house = HouseDetailSerializer(read_only=True)
    buyer = SignUpSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['house', 'buyer', 'phone_number']


class OrderListSerializer(serializers.ModelSerializer):
    house = serializers.SerializerMethodField()
    buyer = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'house', 'buyer', 'order_date', 'phone_number']

    def get_house(self, obj):
        return obj.house.title

    def get_buyer(self, obj):
        return obj.buyer.username


class OrderDetailSerializer(serializers.ModelSerializer):
    house = HouseDetailSerializer(read_only=True)
    buyer = SignUpSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'house', 'buyer', 'order_date', 'phone_number']





