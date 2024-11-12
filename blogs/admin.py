from django.contrib import admin
from .models import House, Order


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'location', 'area', 'bedrooms', 'bathrooms', 'is_sold')
    search_fields = ('title', 'price', 'location', 'area', 'bedrooms', 'bathrooms', 'is_sold')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'house', 'order_date', 'phone_number')
    search_fields =('id', 'buyer', 'house', 'order_date', 'phone_number')


admin.site.register(House, BlogAdmin)
admin.site.register(Order, OrderAdmin)
