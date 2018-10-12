from django.db import models

# Create your models here.

# Category model

class Category(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

# SubCategory Model
# Category are foreign keys
class SubCategory(models.Model):
	name = models.CharField(max_length = 100)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

# Product Model
# Category and subcategory are foreign keys
class Product(models.Model):
	name = models.CharField(max_length = 100)
	# category = models.ForeignKey(Category, on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

	def __str__(self):
		return self.name 