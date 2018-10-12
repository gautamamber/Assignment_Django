"""ProductApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from product_category import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('category/',views.Category_list),
    # path('category/<int:pk>/',views.Category_list.as_view()),
    path('subcategory/',views.SubCategory_list),
    # path('subcategory/<int:pk>/',views.SubCategory_list.as_view()),
    path('product/',views.Product_list),
    # path('product/<int:id>/',views.Product_list.as_view()),
    # url(r'^product/(?P<pk>\d+)$', views.Product_list.as_view(),    name='Product_list'),
    # url(r'^category' , views.Category_list.as_view()),
    # url(r'^subcategory' , views.SubCategory_list.as_view()),
    # url(r'^product' , views.Product_list.as_view()),

    ]
urlpatterns = format_suffix_patterns(urlpatterns)
