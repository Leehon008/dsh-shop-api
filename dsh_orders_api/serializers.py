from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['revenue', 'price','quantity',
        'status','created','updated','owner']
        owner = serializers.ReadOnlyField(source='owner.username')
         