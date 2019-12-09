""" API views for the catalog app """

from rest_framework import generics  # pylint: disable=E0401

from . import models
from . import paginations
from . import serializers

__author__ = 'Umme Nur Tubba'
__copyright__ = 'Copyright 2019'


# Product API View
class ProductListAPIView(generics.ListAPIView):
    """
    Product List API View
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = paginations.ProductListResultsSetPagination


class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    Product Detail API View
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_fields = ['pk', 'slug']


# Product Attribute API View
class ProductAttributeCreateAPIView(generics.CreateAPIView):
    """
    Product Attribute Create API View
    """
    queryset = models.ProductAttribute.objects.all()
    serializer_class = serializers.ProductAttributeCRUDSerializer


class ProductAttributeListAPIView(generics.ListAPIView):
    """
    Product Attribute List API View
    """
    queryset = models.ProductAttribute.objects.all()
    serializer_class = serializers.ProductAttributeSerializer


# Product Price API View
class ProductPriceCreateAPIView(generics.CreateAPIView):
    """
    Product Price Create API View
    """
    queryset = models.ProductPrice.objects.all()
    serializer_class = serializers.ProductPriceCRUDSerializer


class ProductPriceListAPIView(generics.ListAPIView):
    """
    Product Price List API View
    """
    queryset = models.ProductPrice.objects.all()
    serializer_class = serializers.ProductPriceSerializer
