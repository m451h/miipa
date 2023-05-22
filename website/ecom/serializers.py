
from rest_framework import serializers
from ecom.models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description']