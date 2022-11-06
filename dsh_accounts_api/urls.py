#!/usr/bin/python
from django.urls import path
from  .views import UserViewSet as account_views
from rest_framework.urlpatterns import format_suffix_patterns

user_list = account_views.as_view({
    'get': 'list'
})
user_detail = account_views.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])