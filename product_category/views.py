from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from rest_framework.response import Response
from .models import Category, SubCategory, Product
from .serializers import CategoryAPI, SubCategoryAPI, ProductAPI
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.

# Rest api function (GET , POST ) for Category which includes get request, post request

@api_view(['GET', 'POST'])
def Category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategoryAPI(category, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        category = CategoryAPI(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)

#  Rest api function (GET , POST ) for SubCategory which includes get request, post request

@api_view(['GET', 'POST'])
def SubCategory_list(request):
    if request.method == 'GET':
        subcategory = SubCategory.objects.all()
        serializer = SubCategoryAPI(subcategory, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        subcategory =  SubCategoryAPI(data=request.data)
        if subcategory.is_valid():
            subcategory.save()
            return Response(subcategory.data, status=status.HTTP_201_CREATED)
        return Response(subcategory.errors, status=status.HTTP_400_BAD_REQUEST)

#  Rest api function (GET , POST ) for Products which includes get request, post request

@api_view(['GET', 'POST'])
def Product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductAPI(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        product = ProductAPI(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
