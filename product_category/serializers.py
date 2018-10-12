from rest_framework import serializers
from .models import Category, SubCategory, Product

class CategoryAPI(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('name',)

class SubCategoryAPI(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ('name', 'category',)

class ProductAPI(serializers.ModelSerializer):
	class Meta:
		model = Product 
		fields = ('name',  'subcategory',)
