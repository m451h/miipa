from rest_framework import viewsets
from ecom.models import *
from ecom.serializers import * 
import requests
from django.shortcuts import render

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def home(request):
    response = requests.get('http://127.0.0.1:8000/api/product_item/')
    data = response.json()
    return render(request, 'home.html', {'data':data})