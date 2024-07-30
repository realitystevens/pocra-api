from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer




def index(request):
    return JsonResponse({"message": "Pocra Digital Store API"})


class ProductList(generics.ListAPIView):
    queryset = Product.objects.filter(is_published=True)
    serializer_class = ProductSerializer
