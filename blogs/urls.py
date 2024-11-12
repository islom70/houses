from django.urls import path
from blogs.views import house_list_view, house_detail_view, order_list_view, house_create_view, house_update_view, \
    house_delete_view, staff_house_list_view, staff_house_detail_view, order_detail_view, order_delete_view

urlpatterns = [
    path('house/list/', house_list_view, name='house_list'),
    path('house/detail/<int:pk>/', house_detail_view, name='house_detail'),

    path('staff/house/list/', staff_house_list_view, name='staff_house_list'),
    path('staff/house/detail/<int:pk>/', staff_house_detail_view, name='staff_house_detail'),
    path('staff/house/create/', house_create_view, name='house_create'),
    path('staff/house/update/<int:pk>/', house_update_view, name='house_update'),
    path('staff/house/delete/<int:pk>/', house_delete_view, name='house_delete'),

    path('staff/order/list/', order_list_view, name='order_list'),
    path('staff/order/detail/<int:pk>/', order_detail_view, name='order_detail'),
    path('staff/order/delete/<int:pk>/', order_delete_view, name='order_delete')
]
