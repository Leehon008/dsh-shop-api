#!/usr/bin/python
from django.urls import include, path
from .views import OrderViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
order_highlight = OrderViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('orders/', order_list, name='order-list'),
    path('orders/<int:pk>/', order_detail, name='order-detail'),
    path('orders/<int:pk>/highlight/', order_highlight, name='order-highlight'),
])