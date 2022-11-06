from .models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name','slug']
        owner = serializers.ReadOnlyField(source='owner.username')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 
        'image','description','price','stock',
        'available','created','updated','owner']
        